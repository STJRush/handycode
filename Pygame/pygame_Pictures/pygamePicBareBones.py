#starts pygame
from time import sleep
import pygame
pygame.init()

#sets the window size
gameDisplay = pygame.display.set_mode((800,600))

#loads in your pics to use later
castleBackground = pygame.image.load('castleFile.jpg')

mapPinIcon = pygame.image.load('pinFile.png')

#DISPLAY BACKGROUND
gameDisplay.blit(castleBackground, (0,0))
pygame.display.update()
sleep(1)

#DISPLAY YOU ARE HERE
gameDisplay.blit(mapPinIcon, (150,10))
pygame.display.update()
sleep(5)

#GAME WILL NOW EXIT UNLESS YOU LOOP IT OR ADD AN input

pygame.quit()
quit()


# Find maps at https://www.reddit.com/r/battlemaps/top/?t=all
