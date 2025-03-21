import openai
import random

from secrets import *

# Replace with thy most sacred OpenAI API key


# A list of names most noble and enigmatic
npc_names = ["Benedict", "Horatio", "Cassius", "Lysander", "Orlando"]
npc_name = random.choice(npc_names)

# Conversation history to preserve the flow of dialogue
conversation_history = [
    {"role": "system", "content": f"Thou art a cryptic NPC of old, steeped in the tongue of Shakespeare. Reveal not thy name with ease. Speak in poetic riddles and jests, giving only cryptic hints. If the player doth guess truly, thou may’st concede, but not without flair!"}
]

# Function to converse with the Shakespearean NPC
def talk_to_npc(user_input):
    global conversation_history
   
    # Add user input to history
    conversation_history.append({"role": "user", "content": user_input})
   
    # Generate NPC’s response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history,
        max_tokens=150
    )
   
    # Retrieve and return response
    npc_response = response["choices"][0]["message"]["content"].strip()
   
    # Append NPC’s reply to conversation history
    conversation_history.append({"role": "assistant", "content": npc_response})
   
    return npc_response

# The game begins!
print("🎭 Hail, traveller! Thou stand’st before a wanderer most cryptic. 🎭")
print("Prithee, seek my name if thou dost wish, but know this: I yield it not with ease! Type 'exit' to flee.")

while True:
    user_input = input("\nThou: ")
   
    if user_input.lower() == "exit":
        print("NPC: Away dost thou go? Fie! The truth of my name shall ne’er grace thine ears!")
        break
   
    npc_response = talk_to_npc(user_input)
    print("NPC:", npc_response)
   
    # If the user guesses correctly
    if npc_name.lower() in user_input.lower():
        print(f"NPC: Aha! A cunning wit art thou! ‘Tis true, I am {npc_name}. Thou hast unmasked me at last! 🎭")
        break
