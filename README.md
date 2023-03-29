# Computer Vision Snake

This is a self-driven practice project to re-enforce the learnings from the ["Rock, Paper, Scissors"](https://github.com/MartinKlefas/computer-vision-rock-paper-scissors) coursework assignment from AICore. I've tried to implement more readable code, and coding best practices, while rehearsing some of the structures and concepts learned so far. 

The ultimate aim is to have a playable version of snake, controlled by moving a printed or drawn arrow to the direction you want your snake to go in.

# Choices made

 - Train a Tensorflow Lite Model locally to learn a little more about the backend processes and considerations that will affect model quality
 - Create a more robust model that can understand inputs from other people and potentially other cameras
 - Leave the code in modules and functions rather than making a fully OO / class based version 
	 - This is simply as it's more in keeping with the lesson. The next lessons revolve more around OO programming.
  
 # Progress
The game will now play in a rudimentary sense. Having created key-based controls the snake will traverse the playing field, followed by a single body section, and make a series of turns. The body section follows the turn-history of the head, turning at the appropriate point in the head's historical path.

I have made a [repository here](https://github.com/MartinKlefas/tensorflow_trainer) to help in taking the appropriate training images, and in training the subsequent model. It does also do rudimentary tests on the model before passing back the model files to be used here.

The model has been included into the code base and will now also control the snake in the same way as the keyboard. There's no rate limitation at present, which means you'll effectively be able to turn as fast and often as your computer can use TFLite to make a prediction about what is sees.

The model itself tests fine, but unfortunately doesn't seem to want the snake to go "right" very often.

I've made an alternative implementation of the snake game itself, that more closely matches it's usual implementation. It's very basic graphically at present, but the code allows for a growing snake, scores and "food". This needs a bit more testing, before modularisation to use the vision model can take place.

# To Do

 1. Modularise new snake game code
 2. Implement test/validate schema with tensorboard feedback on model training.
 3. Retrain the model to make the snake go "Right" when it should do


> Written with [StackEdit](https://stackedit.io/).