# if you find the key at the beach, you can use it in the mountain

import random
import pygame
import cv2
import threading

######## ######## ######## ######## NEW CODE FOR MUSIC
# Initialize pygame mixer
pygame.mixer.init()

def play_music_for(location_name):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(location_name + ".mp3")
    pygame.mixer.music.play(-1)
######## ######## ######## ######## 

######## ######## ######## ######## NEW CODE FOR VIDEO INTRO USING OPENCV (Looped)
def play_video_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Island of Moray")

    video = cv2.VideoCapture('intro.mp4')

    while True:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            frame = cv2.resize(frame, (800, 600))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pygame_frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            screen.blit(pygame_frame, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    video.release()
                    pygame.quit()
                    return

video_thread = threading.Thread(target=play_video_loop, daemon=True)
video_thread.start()
######## ######## ######## ######## 

# make your list
bag_list = []

def intro():
    print(r"""
 _____ _ _   _      
|_   _(_) |_| | ___ 
  | | | | __| |/ _ \
  | | | | |_| |  __/
  |_| |_|\__|_|\___|
""")
    input("Press Enter to Start")
    beach()

# Your first location
def beach():
    play_music_for("beach")
    print("You get to the (b)each 🏖️")
   
    beach_loot = ["gold", "eggs", "old key"]
   
    print("Inventory", bag_list)
    print("You find something!")
    bag_list.append(random.choice(beach_loot))
    print("Inventory", bag_list)
   
    choice = input("""
    - Go to the (m)ountains
    - Go to the (f)orest
    """)
   
    if choice == "m":
        print("You start climbing up...")
        mountains()
    elif choice == "f":
        print("You wander into the trees...")
        forest()
    else:
        print("What? That's not an option")
        beach()

def forest():
    play_music_for("forest")
    print("You get to the (f)orest 🌲")
   
    choice = input("""
    - Go to the (m)ountains
    - Go to the (b)each
    """)
   
    if choice == "m":
        print("You start climbing up...")
        mountains()
    elif choice == "b":
        print("You head out to the beach...")
        beach()
    else:
        print("What? That's not an option")
        forest()

def mountains():
    play_music_for("mountains")
    print("You get up to the top of the mountains 🌋")

    if "old key" in bag_list:
        print("You see a keyhole in the mountainside")
        print("you try your key and it opens")
        secret_room()
    else:
        print("You see a keyhole in the mountainside")
        print("You don't have any keys yet")

    choice = input("""
    - Go to the (f)orest
    - Go to the (b)each
    """)

    if choice == "m":
        print("You start climbing up...")
        mountains()
    elif choice == "b":
        print("You head out to the beach...")
        beach()
    else:
        print("What? That's not an option")
        mountains()

def death():
    print("U ded")
    print("You died so much, you crash python")
    raise Exception

def victory():
    print("U win, go you.")

def secret_room():
    print("Wow the dwarven mines!")
    print("Hopefully there's no dragons in here")
   
    print("There is! FIGHTING TIME!")
   
    dragonHealth = 10
    playerHealth = 10
   
    while dragonHealth > 0 and playerHealth > 0:
   
        choice = input("""what do you want to do?
        - (s)word
        - (b)oot
        """)
       
        if choice == "s":
            print("You use a sword attack")
            damage = random.randint(1,10)
            dragonHealth -= damage
            print("The dragon takes..", damage, "sword damage")
        elif choice == "b":
            print("You throw your boot")
            damage = random.randint(2,3)
            dragonHealth -= damage
            print("The dragon takes..", damage, "boot damage")
        else:
            print("Now is not the time for that")

        print("The dragon uses MORNING BREATH")
        damage = random.randint(2,6)
        playerHealth -= damage
       
        print("Your health is...", playerHealth)
        print("The BBEG's Health is...", dragonHealth)
       
    if playerHealth <= 0:
        death()
    elif dragonHealth <= 0:
        victory()

################################################################################        
intro()
