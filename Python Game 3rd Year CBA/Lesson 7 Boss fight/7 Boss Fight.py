# if you find the key at the beach, you can use it in the mountain

import random

# make your list
bag_list = []

# Your first location
def beach():

    print("You get to the (b)each 🏖️")
    
    # this is a loot list of things a player can find at the beach
    beach_loot = ["gold", "eggs", "old key"]
    
    # add the treasure
    print("Inventory",bag_list)
    print("You find something!")
    bag_list.append(random.choice(beach_loot)) # pick a random item from the loot list
    print("Inventory",bag_list)
    

    choice = input("""
    - Go to the (m)mountains
    - Go to the (f)orest
    """)

    if choice == "m":
        print("You start climbing up...")
        mountains() #  goes to this location
        
    elif choice == "f":
        print("You wander into the trees...")
        forest() #  goes to this location
        
    else:
        print("What? That's not an option")
        beach() #  replays this location
        
        
# Your second location
def forest():

    print("You get to the (f)orest 🌲")

    choice = input("""
    - Go to the (m)ountains
    - Go to the (b)each
    """)

    if choice == "m":
        print("You start climbing up...")
        mountains() #  goes to this location
        
    elif choice == "b":
        print("You head out to the beach...")
        beach() #  goes to this location
        
    else:
        print("What? That's not an option")
        forest() #  replays this location
        
        
# Your third location
def mountains():

    print("You get up to the top of the mountains 🌋")
    
    ###### This function checks if you have the key
    print("You see a keyhole in the mountainside")
    if "old key" in bag_list:
        print("You see a keyhole in the mountainside")
        print("you try your key and it opens")
        secret_room() # calls the secret room function to bring you there
    else:
        print("You don't have any keys yet")
        
    


    choice = input("""
    - Go to the (f)orest
    - Go to the (b)each
    """)

    if choice == "m":
        print("You start climbing up...")
        mountains() #  goes to this location
        
    elif choice == "b":
        print("You head out to the beach...")
        beach() #  goes to this location
        
    else:
        print("What? That's not an option")
        mountains() #  replays this location
    
def secret_room():
    print("Wow the dwarven mines!")
    print("Hopefully there's no dragons in here")
    
    print("There is! FIGHTING TIME!")
    
    dragonHealth = 10
    playerHealth = 10
    
    # only keep playing while player and boss are alive
    while dragonHealth > 0 AND playerHealth > 0:
    
        choice = input("""what do you want to do?
        - (s)word
        - (b)oot
        - (r)un
        """)
        
        if choice == "s":
            print("You use a sword attack")
            damage = random.randint(1,10)
            dragonHealth = dragonHealth - damage
            print("The dragon takes..", damage, "damage")
    
    
    
    
        
################################################################################        
# Your program starts here by calling the whatever function you want to start at:
beach()
