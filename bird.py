import pygame
import sys 
import time 
import random


pygame.init()

# Set up the screen
height = 600
width = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harun GAMES")

# mengubah warna screen
screen.fill((220, 0,0))

# membuat lingkaran


# Game variables
running = True
clock = pygame.time.Clock()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic and rendering here

    pygame.display.update()

pygame.quit()



