# add inventory

# make your list
bag_list = []

# Your first location
def beach():

    print("You get to the (b)each 🏖️")
    
    # add the treasure
    print("Inventory",bag_list)
    print("You find a shell!")
    bag_list.append("Shell")
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
        
        
################################################################################        
# Your program starts here by calling the whatever function you want to start at:
beach()
