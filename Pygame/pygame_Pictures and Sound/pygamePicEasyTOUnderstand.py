#starts pygame
from time import sleep
import pygame
pygame.init()

#sets the window size
gameDisplay = pygame.display.set_mode((800,600))

#loads in your pics to use later
pokeScreen1 = pygame.image.load('village.PNG')
garyImg = pygame.image.load('gary.png')

#SET BACKGROUND COLOUR
gameDisplay.fill((0,0,0)) # paints black


#DISPLAY PICS
sleep(1)
print("Loading Background screen")
gameDisplay.blit(pokeScreen1, (80,80))
pygame.display.update()
 #puts pokemon background at 
sleep(2)


print("Displaying Picture of Gary at x,y (0,0)")
gameDisplay.blit(garyImg, (0,0))
sleep(3)
print("Ooops! It's loaded but I forgot to update the display like before!")
sleep(1)
print("So paste in this every time: pygame.display.update()")
sleep(2)

pygame.display.update()
print("There we go!")
sleep(3)

print("Now I'll change the x co-ordinate to move him right")
sleep(2)

# Moves picture right
gameDisplay.blit(garyImg, (0,0)) #puts a pokemon trainer picture at these x,y co-ordinates
pygame.display.update()
sleep(0.5)

gameDisplay.blit(garyImg, (30,0)) #puts a pokemon trainer picture at these x,y co-ordinates
pygame.display.update()
sleep(0.5)

gameDisplay.blit(garyImg, (60,0)) #puts a pokemon trainer picture at these x,y co-ordinates
pygame.display.update()
sleep(3)

print("Wait why is he copying himself?")
sleep(2)
print("Oh wait the old pictures are not being removed")#
sleep(2)
print("I need to load the background image each time again to cover up the old gary!")
sleep(2)
print("So 1. display background, 2. display picture on top, 3. update display, 3 IN THAT ORDER ")
sleep(2)
print("Let's try change the y value and move him down")
sleep(2)

#fills in background to stop duplicates
gameDisplay.blit(pokeScreen1, (80,80))


# Moves picture down
gameDisplay.blit(pokeScreen1, (80,80)) #display background pic to cover up other stuff
gameDisplay.blit(garyImg, (0,0)) #puts a pokemon trainer picture at these x,y co-ordinates
pygame.display.update() # update to actually show any changes you've made
sleep(0.5)

gameDisplay.blit(pokeScreen1, (80,80)) #display background pic to cover up other stuff
gameDisplay.blit(garyImg, (0,20)) #puts a pokemon trainer picture at these x,y co-ordinates
pygame.display.update() # update to actually show any changes you've made
sleep(0.5)

gameDisplay.blit(pokeScreen1, (80,80)) #display background pic to cover up other stuff
gameDisplay.blit(garyImg, (0,40)) #puts a pokemon trainer picture at these x,y co-ordinates
pygame.display.update() # update to actually show any changes you've made
sleep(1)


#NAME                    
print("Your program is ready to go here now")
sleep(1)

print("Until then, it's game over!")
sleep(1)

pygame.quit()
quit()
