import tkinter as tk
from PIL import Image, ImageTk
import random

# =====================
# GLOBAL VARIABLES
# =====================

bag_list = []          # The player's inventory (list of found items)
dragonHealth = 10      # Dragon's health in the secret room
playerHealth = 10      # Player's health in the secret room

# We'll store references to images so they don't get garbage-collected
images = {}

# =====================
# HELPER FUNCTIONS
# =====================

def load_images():
    """
    Load and resize all the PNG images using PIL (Pillow).
    We'll store them in the 'images' dictionary.
    Each image is resized to 600x600 pixels.
    """
    # 'ANTIALIAS' is a high-quality downsampling filter (in newer Pillow versions, use 'Resampling.LANCZOS')
    
    # Beach
    beach_img = Image.open("beachpic.png").resize((600, 600))
    images['beach'] = ImageTk.PhotoImage(beach_img)
    
    # Forest
    forest_img = Image.open("forestpic.png").resize((600, 600))
    images['forest'] = ImageTk.PhotoImage(forest_img)
    
    # Mountains
    mountains_img = Image.open("mountainspic.png").resize((600, 600))
    images['mountains'] = ImageTk.PhotoImage(mountains_img)
    
    # Secret Room
    secret_room_img = Image.open("secret_roompic.png").resize((600, 600))
    images['secret_room'] = ImageTk.PhotoImage(secret_room_img)
    
    # Death
    death_img = Image.open("deathpic.png").resize((600, 600))
    images['death'] = ImageTk.PhotoImage(death_img)
    
    # Victory
    victory_img = Image.open("victorypic.png").resize((600, 600))
    images['victory'] = ImageTk.PhotoImage(victory_img)

def set_background(image_key):
    """
    Update the background image of the main window
    using one of the loaded images (600x600).
    """
    bg_label.config(image=images[image_key])
    bg_label.image = images[image_key]  # Keep a reference

def set_text(text):
    """
    Update the main text label with new text.
    """
    main_text.config(text=text)

def clear_buttons():
    """
    Remove any buttons that were previously packed in the button_frame.
    """
    for widget in button_frame.winfo_children():
        widget.destroy()

def update_inventory():
    """
    Show the player's inventory in the inventory_label.
    """
    inventory_label.config(text="Inventory: " + str(bag_list))

# =====================
# LOCATION FUNCTIONS
# =====================

def beach():
    """
    The first location: The Beach.
    A random item is found automatically. Then the player can choose
    to go to the mountains or the forest.
    """
    clear_buttons()            # Remove old buttons
    set_background("beach")    # Beach background
    set_text("You are at the Beach 🏖️\nYou find something in the sand!")
    
    # Add random item to bag_list
    beach_loot = ["gold", "eggs", "old key"]
    found_item = random.choice(beach_loot)
    bag_list.append(found_item)
    
    # Update inventory display
    update_inventory()
    
    # Create buttons to go to Mountains or Forest
    btn_mountains = tk.Button(button_frame, text="Go to Mountains", command=mountains, font=("Arial", 12))
    btn_mountains.pack(side=tk.LEFT, padx=10, pady=10)
    
    btn_forest = tk.Button(button_frame, text="Go to Forest", command=forest, font=("Arial", 12))
    btn_forest.pack(side=tk.LEFT, padx=10, pady=10)

def forest():
    """
    The Forest location. You can choose to go to the Mountains or back to the Beach.
    """
    clear_buttons()
    set_background("forest")
    set_text("You are in the Forest 🌲")
    update_inventory()
    
    # Buttons for next locations
    btn_mountains = tk.Button(button_frame, text="Go to Mountains", command=mountains, font=("Arial", 12))
    btn_mountains.pack(side=tk.LEFT, padx=10, pady=10)
    
    btn_beach = tk.Button(button_frame, text="Go to Beach", command=beach, font=("Arial", 12))
    btn_beach.pack(side=tk.LEFT, padx=10, pady=10)

def mountains():
    """
    The Mountains location. Checks if you have the 'old key'.
    If so, you can enter the secret room automatically.
    Otherwise, you can go to the Forest or Beach.
    """
    clear_buttons()
    set_background("mountains")
    set_text("You are at the Mountains 🌋\nYou see a keyhole in the mountainside.")
    update_inventory()
    
    # If the player has the old key, go to secret_room automatically
    if "old key" in bag_list:
        set_text("You used the 'old key' to open a hidden door!\nEntering the Secret Room...")
        # We can add a short delay before going to the secret room
        root.after(1500, secret_room)  # 1.5 second delay
    else:
        # If no key, show the usual buttons
        btn_forest = tk.Button(button_frame, text="Go to Forest", command=forest, font=("Arial", 12))
        btn_forest.pack(side=tk.LEFT, padx=10, pady=10)
        
        btn_beach = tk.Button(button_frame, text="Go to Beach", command=beach, font=("Arial", 12))
        btn_beach.pack(side=tk.LEFT, padx=10, pady=10)

def secret_room():
    """
    The Secret Room location. Dragon fight!
    Player chooses sword or boot attacks until either the dragon or player
    runs out of health.
    """
    clear_buttons()
    set_background("secret_room")
    
    # We have to declare we want to modify these globals
    global dragonHealth
    global playerHealth
    
    def update_battle_text(msg=""):
        """
        Show current health and any extra message about attacks.
        """
        text_to_show = (
            "You are in the Secret Room!\n"
            "A dragon is here! FIGHT!\n\n"
            f"Your Health: {playerHealth}\n"
            f"Dragon's Health: {dragonHealth}\n"
        )
        if msg:
            text_to_show += "\n" + msg
        set_text(text_to_show)
    
    # Show initial state
    update_battle_text()
    
    def sword_attack():
        global dragonHealth, playerHealth
        damage = random.randint(1, 10)
        dragonHealth -= damage
        message = f"You slash the dragon with a sword for {damage} damage!"
        
        # Check if dragon is defeated
        if dragonHealth <= 0:
            victory()
            return
        
        # Dragon attacks back
        d_damage = random.randint(2, 6)
        playerHealth -= d_damage
        message += f"\nDragon uses MORNING BREATH for {d_damage} damage on you!"
        
        if playerHealth <= 0:
            death()
            return
        
        update_battle_text(message)
    
    def boot_attack():
        global dragonHealth, playerHealth
        damage = random.randint(2, 3)
        dragonHealth -= damage
        message = f"You throw your boot at the dragon for {damage} damage!"
        
        # Check if dragon is defeated
        if dragonHealth <= 0:
            victory()
            return
        
        # Dragon attacks back
        d_damage = random.randint(2, 6)
        playerHealth -= d_damage
        message += f"\nDragon uses MORNING BREATH for {d_damage} damage on you!"
        
        if playerHealth <= 0:
            death()
            return
        
        update_battle_text(message)
    
    # Create attack buttons
    btn_sword = tk.Button(button_frame, text="Sword Attack", command=sword_attack, font=("Arial", 12))
    btn_sword.pack(side=tk.LEFT, padx=10, pady=10)
    
    btn_boot = tk.Button(button_frame, text="Boot Attack", command=boot_attack, font=("Arial", 12))
    btn_boot.pack(side=tk.LEFT, padx=10, pady=10)

def death():
    """
    Called when the player dies.
    """
    clear_buttons()
    set_background("death")
    set_text("U ded\nYou died so much, you crashed python!")
    
    # Button to exit
    btn_exit = tk.Button(button_frame, text="Exit Game", command=root.destroy, font=("Arial", 12))
    btn_exit.pack(side=tk.LEFT, padx=10, pady=10)

def victory():
    """
    Called when the dragon is defeated.
    """
    clear_buttons()
    set_background("victory")
    set_text("U win, go you!")
    
    # Button to exit
    btn_exit = tk.Button(button_frame, text="Exit Game", command=root.destroy, font=("Arial", 12))
    btn_exit.pack(side=tk.LEFT, padx=10, pady=10)

# =====================
# TKINTER SETUP
# =====================

root = tk.Tk()
root.title("Adventure Game (Scaled Images)")

# Load all images at startup
load_images()

# Create a label for the background
bg_label = tk.Label(root)
bg_label.pack()

# Create a label for the main text (with larger font)
main_text = tk.Label(root, text="", width=60, height=6, wraplength=500, justify="left", font=("Arial", 14))
main_text.pack(pady=10)

# Create a label to show the inventory (with slightly bigger font)
inventory_label = tk.Label(root, text="Inventory: []", font=("Arial", 12))
inventory_label.pack(pady=5)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# =====================
# START THE GAME
# =====================
beach()  # Begin at the beach

root.mainloop()
