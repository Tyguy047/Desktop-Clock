import pygame
import datetime
import sys
import os

pygame.init()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Desktop Clock")

# Set up the fonts
date_font = pygame.font.SysFont('hensa', 40)
time_font = pygame.font.SysFont('hensa', 60)

# Set up the clock
clock = pygame.time.Clock()

# Set the icon file path
icon_path = os.path.join(os.path.dirname(__file__), "icon.icns")

# Set the icon for the application window
pygame.display.set_icon(pygame.image.load(icon_path))

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current date and time
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
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
