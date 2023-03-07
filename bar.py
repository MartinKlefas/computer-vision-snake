import pygame
import sys
import settings

import cv2
import tensorflow as tf
import numpy as np

scalar_speed = settings.scalar_speed
Directions = {"Left": [-1*scalar_speed,0], "Right": [scalar_speed,0], "Up":[0,-1*scalar_speed], "Down": [0,scalar_speed]}

def getDirection():
    for event in pygame.event.get():
       
       if event.type == pygame.QUIT:
           sys.exit()
       elif event.type == 32787:
           sys.exit
       
       
       elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return Directions["Left"]
            elif event.key == pygame.K_RIGHT:
                return Directions["Right"]
            elif event.key == pygame.K_UP:
                return Directions["Up"]
            elif event.key == pygame.K_DOWN:
                return Directions["Down"]
            elif event.key == pygame.K_a:
                return Directions["Left"]
            elif event.key == pygame.K_d:
                return Directions["Right"]
            elif event.key == pygame.K_w:
                return Directions["Up"]
            elif event.key == pygame.K_s:
                return Directions["Down"]
            elif event.key == pygame.K_q:
                sys.exit()
            else:
                return ""
       else:
           return ""

model = None
cap = None

input_details = None
output_details = None

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
labels = list()

def initVision():
    global model 
    # Load TFLite model and allocate tensors.
    model = tf.contrib.lite.Interpreter(model_path="model.tflite")

    global input_details, output_details
    # Get input and output tensors.
    input_details = model.get_input_details()
    output_details = model.get_output_details()

    model.allocate_tensors()

    global cap
    cap = cv2.VideoCapture(0)
    f = open('labels.txt', 'r')

    try:
        lines = f.readlines()
        global labels
        for line in lines:
            labels.append(line.split(" ")[1].rstrip('\n'))
        
    finally:
        f.close()
    

def visionGetDirection():
    if model == None:
        initVision()
    
    tDirection = get_prediction()
    return Directions[tDirection]
    



def get_prediction(): 
    strPrediction = "Nothing"   
    while strPrediction == "Nothing" :
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)

        model.set_tensor(input_details[0]['index'],[resized_frame])

        model.invoke()
        
        prediction = model.get_tensor(output_details[0]['index'])

        cv2.imshow('Camera Controller', frame)
        strPrediction = labels[np.argmax(prediction)]
            
    print("You Chose: ", strPrediction)
    return strPrediction

