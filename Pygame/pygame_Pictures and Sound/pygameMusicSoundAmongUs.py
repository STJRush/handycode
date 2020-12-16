#sets up pygame
from time import sleep
import pygame
pygame.init()

#sets up pygame music
from pygame import mixer
mixer.init()

#Loads the music file
mixer.music.load("funeral.mp3") # This .mp3 needs to be in the same folder as your .py python file
 
mixer.music.play()

#sets the window size
gameDisplay = pygame.display.set_mode((800,600))

#loads in your pics to use later
starrynight = pygame.image.load('spaced1.PNG')
greendude = pygame.image.load('lightgreend.PNG')

#DISPLAY SCROLLING SPACE BACKGROUND

for x in range(0,50):
    gameDisplay.blit(starrynight, (-x,0))  
    pygame.display.update()
    sleep(0.11)

# Why is it -x? : I changed this to minus to scroll right instead of 
# left because I was running out of picture when it scrolled the other way

# In the next for loop I had to then start at -50 because the space background
# was jumping back to 0,0. It has to start where it left off scrolling.


#DISPLAY THE LIGHTGREEN GUY BEING SPACED

for x in range(13):
    gameDisplay.blit(starrynight, (-50,0))  # covers up clones. Try comment this out.
    gameDisplay.blit(greendude, (0,x)) # shows the green dude. X position changes each time.
    greendude = pygame.transform.rotate(greendude,500) # Rotates him around
    pygame.display.update() # actually shows the changes from the previous lines of code
    sleep(0.45) # took me a while to get the music in sync!

pygame.quit()
quit()
