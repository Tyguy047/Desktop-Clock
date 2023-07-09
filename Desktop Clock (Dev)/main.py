# Coded and Developed By: Tyler Caselli with help from Chat GPT
# Coded In VS Code with Python on M1 MacBook Air (8gb Ram 256gb Storage)

import pygame
import datetime
import sys

pygame.init()

# Set up the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Desktop Clock")

# Set up the fonts
date_font = pygame.font.SysFont('hensa', 60)
time_font = pygame.font.SysFont('hensa', 90)

# Set up the clock
clock = pygame.time.Clock()

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current date and time
    now = datetime.datetime.now()
    date_str = now.strftime("%m/%d/%Y")
    time_str = now.strftime("%H:%M:%S")

    # Render the text
    date_surface = date_font.render(date_str, True, pygame.Color('white'))
    time_surface = time_font.render(time_str, True, pygame.Color('white'))

    # Clear the screen and draw the text
    screen.fill(pygame.Color('#02569b'))
    screen.blit(date_surface, (WINDOW_WIDTH/2 - date_surface.get_width()/2, WINDOW_HEIGHT/2 - date_surface.get_height()))
    screen.blit(time_surface, (WINDOW_WIDTH/2 - time_surface.get_width()/2, WINDOW_HEIGHT/2))

    # Update the display and wait for the next frame
    pygame.display.flip()
    clock.tick(60)
