import pygame

pygame.init()

# Get the list of fonts
fonts = pygame.font.get_fonts()

# Print out the list of fonts
for font in fonts:
    print(font)