#starts pygame
from time import sleep
import pygame
pygame.init()

#sets the window size
gameDisplay = pygame.display.set_mode((800,600))

#loads in your pics to use later
pokeScreen1 = pygame.image.load('village.PNG')
garyImg = pygame.image.load('gary.png')

#DISPLAY BACKGROUND
gameDisplay.blit(pokeScreen1, (80,80))
pygame.display.update()
sleep(2)

#DISPLAY GARY
gameDisplay.blit(garyImg, (0,0))
pygame.display.update()
sleep(2)

pygame.quit()
quit()
