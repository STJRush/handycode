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
gameDisplay.blit(pokeScreen1, (0,0))
pygame.display.update()
sleep(1)


#repeats movement 100 times
for leftyrighty in range(0,100): #change "leftyrighty" from 0 to 100

    #DISPLAY GARY
    gameDisplay.blit(pokeScreen1, (0,0)) # load background pic on top to stop mirror images
    gameDisplay.blit(garyImg, (leftyrighty,0)) # load gary pic at position x,y with x changing (renamed it leftyrighty)
    pygame.display.update() # actually show changes
    sleep(0.005) #add a pause so it's not totally instant

pygame.quit()
quit()

