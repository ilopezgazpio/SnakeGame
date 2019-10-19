#!/usr/bin/python

import pygame
import sys
import random
import time

# Initialize pygame
check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)

# Game surface
play_surface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game')

# Colors (r,g,b)
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

# Frame controller (FPS)
fps_controller = pygame.time.Clock()

# Snake location
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Food location
food_pos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
food_spawn = True

# Direction variables
direction = 'RIGHT'
change_to = direction

# Score variable
score = 0

# Game Over function
def gameOver():
    my_font = pygame.font.SysFont('arial', 72)
    GOsurface = my_font.render('Game Over!', True, red)
    Gorectangle = GOsurface.get_rect()
    Gorectangle.midtop = (720/2, 15)
    play_surface.blit(GOsurface, Gorectangle)
    pygame.display.flip()
    showScore(choice=0)
    time.sleep(4)
    pygame.quit()
    sys.exit(0)

def showScore(choice = 1):
    my_score_font = pygame.font.SysFont('arial', 24)
    SCOREsurface = my_score_font.render('Score: {0}'.format(score), True, black)
    SCORErectangle = SCOREsurface.get_rect()
    if choice == 1:
        SCORErectangle.midtop = (80, 10) # Upper left
    else:
        SCORErectangle.midtop = (360, 120) # Below game over message
    play_surface.blit(SCOREsurface, SCORErectangle)

# Main loop of the game
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            elif event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            elif event.key == pygame.K_ESCAPE:
                # create closing event
                pygame.event.post(pygame.event.Event(pygame.QUIT))


    # Validation of direction
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    elif change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update snake location
    if direction == 'RIGHT':
        snake_pos[0] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10

    # Update snake body
    snake_body.insert(0, list(snake_pos)) # insert new location of snake head

    # Snake eats food
    if snake_pos == food_pos:
        food_spawn = False
        score+=1
    else:
        snake_body.pop()

    # Create food
    if food_spawn == False:
        food_pos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    food_spawn = True

    # Graphic things
    play_surface.fill(white) # fill surface with color

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(play_surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(play_surface, brown, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Check snake position in space (out of playable space)
    if snake_pos[0] > 720 - 10 or snake_pos[0] < 0:
        gameOver()
    elif snake_pos[1] > 440 - 10 or snake_pos[1] < 0:
        gameOver()

    # Check Snake collapses with itself
    if snake_pos in snake_body[1:]:
        gameOver()

    # Show score
    showScore()

    # Refresh surface
    pygame.display.flip()

    fps_controller.tick(22)





