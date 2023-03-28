import pygame
import sys
import random
from pygame.locals import *

pygame.init()

font = pygame.font.Font(None, 36)

# Screen dimensions
WIDTH = 640
HEIGHT = 480
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():    
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake Game")

    snake = [(20, 20), (40, 20), (60, 20)]
    snake_direction = (20, 0)
    food = random_food_position(snake)

    clock = pygame.time.Clock()
    grace_period = 101  # player can't kill themselves in the first 10 seconds * 10 ticks per second
    score = 0
    time_elapsed = 0
    while True:
        grace_period -= 1
        time_elapsed += 1
        if time_elapsed % 100 == 0:
            score += 1
        for event in pygame.event.get():
            if event.type == QUIT:                
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in (K_UP, K_w) and snake_direction[1] != 20:
                    snake_direction = (0, -20)
                elif event.key in (K_DOWN, K_s) and snake_direction[1] != -20:
                    snake_direction = (0, 20)
                elif event.key in (K_LEFT, K_a) and snake_direction[0] != 20:
                    snake_direction = (-20, 0)
                elif event.key in (K_RIGHT, K_d) and snake_direction[0] != -20:
                    snake_direction = (20, 0)
                elif event.key in (K_ESCAPE, K_q):
                    game_over(screen, score)


        new_head = ((snake[0][0] + snake_direction[0]) % WIDTH, (snake[0][1] + snake_direction[1]) % HEIGHT)

        snake.insert(0, new_head)

        if snake[0] == food:
            food = random_food_position(snake)
            score += 10
        else:
            snake.pop()


        if grace_period <= 0 and snake[0] in snake[1:]:
                game_over(screen,score)
        
   
        
        screen.fill(BLACK)

        draw_food(screen, food)
        draw_snake(screen, snake)
        draw_score(screen, score)
       
        pygame.display.update()
        clock.tick(10)

def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def random_food_position(snake):
    while True:
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if food not in snake:
            return food
        
def draw_score(screen, score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over(screen, score):
    screen.fill(BLACK)

    # Draw a coiled snake with a red forked tongue
    pixel_size = 4
    snake_pixels = [
        # Body
        (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (18, 4),
        (11, 5), (12, 5), (18, 5), (19, 5), (20, 5),
        (11, 6), (12, 6), (20, 6),
        (11, 7), (20, 7),
        (11, 8), (20, 8),
        (11, 9), (12, 9), (13, 9), (14, 9), (15, 9), (16, 9), (17, 9), (18, 9), (19, 9), (20, 9),
        # Head
        (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3),
        (11, 4), (11, 5), (11, 6),
        # Eyes
        (13, 2), (15, 2),
        # Tongue
        (12, 1), (17, 1), (13, 0), (16, 0),
    ]

    for pixel in snake_pixels:
        if pixel in [(12, 1), (17, 1), (13, 0), (16, 0)]:
            color = RED
        elif pixel in [(13, 2), (15, 2)]:
            color = WHITE
        else:
            color = GREEN

        pygame.draw.rect(screen, color, (pixel[0] * pixel_size, pixel[1] * pixel_size, pixel_size, pixel_size))

    # Show final score
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

    # Show "Press any key to exit" message
    exit_text = font.render("Press any key to exit", True, WHITE)
    screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 40))

    pygame.display.update()

    # Wait for a key press to exit
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()
