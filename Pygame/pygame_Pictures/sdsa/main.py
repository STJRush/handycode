

# DO NOT DELETE THIS CODE
import pygame, sys
from pygame.locals import QUIT
from time import sleep
pygame.init()
gameDisplay = pygame.display.set_mode((400,300))
import random


# NEW CODE THIS LESSON TO INCLUDE MUSIC 
from pygame import mixer 
mixer.init() 

# LOAD IN SOUNDS:

pistol= mixer.Sound("pistol.wav")

# LOAD IN YOUR MUSIC FILE .mp3

mixer.music.load("IntroSong.mp3")

# LOAD AND PLAY THE MUSIC
mixer.music.play()


sleep(2)


##########################################################
# Your intro code goes here

## THE SETUP AND LOADING YOUR FILES FOR LATER

# Change this to your game title
pygame.display.set_caption('RUSH AROUND RUSH v1.0')

# SET BACKGROUND COLOUR using (R,G,B) Red Green Blue
gameDisplay.fill((0,0,0)) # paints black    (255,255,255) would be white


# Loads in all of your pics to use later. You should include this line for all images at the start of your program.
titleScreen = pygame.image.load('titlescreen.png')
gameStudioTitle = pygame.image.load('gameStudio.png')
stevenSegull = pygame.image.load('steves.jpg')
hole = pygame.image.load('hole.png')

# Make the image bigger or smaller by changing the scale. You should include this line for all images at the start of your program. The default for replit is width 400 pixels, height 300 pixels.



# TO SCALE an image to x y values:
# newPicName = pygame.transform.scale(oldPicName, (x,y))

titleScreenScaled = pygame.transform.scale(titleScreen, (400,300))
gameStudioTitleScaled = pygame.transform.scale(gameStudioTitle, (400,300))
stevenSegullScaled = pygame.transform.scale(stevenSegull, (400,300))
holeScaled = pygame.transform.scale(hole, (50,50))


## ACTUALLY SHOWING IMAGES DURING YOUR GAME


# PRESENTS...
gameDisplay.blit(gameStudioTitleScaled, (0,0)) 
pygame.display.update() 

# Waits 2 seconds..
sleep(2.5)

# RUSH AROUND RUSH MAIN TITLE SCREEN
gameDisplay.blit(titleScreenScaled, (0,0))  
pygame.display.update() 

########################################################


print("WELCOME TO MY GAME")
x = input("Press RETURN TO START!")

# Stops the title music
mixer.music.stop()

# load in some new music for the actual game, not the title screen
mixer.music.load("segullBatttleMusic.mp3")
mixer.music.play()

stevenSegullScaled = pygame.transform.scale(stevenSegull, (1300,1000))
gameDisplay.blit(stevenSegullScaled, (0,0))  
pygame.display.update() 


sleep(3.4)

stevenSegullScaled = pygame.transform.scale(stevenSegull, (1000,800))
gameDisplay.blit(stevenSegullScaled, (100,0))  
pygame.display.update() 

sleep(3.4)

stevenSegullScaled = pygame.transform.scale(stevenSegull, (900,700))
gameDisplay.blit(stevenSegullScaled, (0,0))  
pygame.display.update() 


sleep(6.4)

stevenSegullScaled = pygame.transform.scale(stevenSegull, (400,300))
gameDisplay.blit(stevenSegullScaled, (0,0))  
pygame.display.update() 



print("A wild Steven Segull appears! BOSS BATTLE MUSIC TIME!")

while True:
  choice = input("Press p to shoot pistol")


  if choice == "p":
    print("You shoot at Steven Seagull")
    mixer.Sound.play(pistol)

  elif choice == "m":

    print("HEY YOU'VE BEEN READING THE CODE!")
    
    for x in range(8):
      mixer.Sound.play(pistol)
      gameDisplay.blit(holeScaled, (random.randint(1,300),random.randint(1,300)))  
      pygame.display.update()
      sleep(0.2)

  else: 
    print("You had one job...")

