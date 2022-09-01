
# This program takes a variable (playerGuess here but could be any serial data) from a microbit and brings it into Thonny. 
# USB Serial data comes with lots of junk text like \\r\\n so most of this program is for cleaning those parts away leaving just the variable we want.

import serial
from time import sleep
from random import choice



ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"

print("Type CTRL + C to exit. (may take 5 seconds)")

# Opens the packet of crunchie nut cornflakes
ser.open()

computerPoints = 0
playerPoints = 0

# Try this unless you hit CTL+C
try:
    
    # In fact... keep trying it! Again and again! MOAR!
    while True:
        
        # Try read the serial data
        try:
            
            # First take in all the data and assign it to this variable
            microbitdata = str(ser.readline())
            
            # Get second bit onwards, call that playerGuess
            playerGuess = microbitdata[2:]
            
            # Remove any spaces
            playerGuess = playerGuess.replace(" ","")
            
            # Remove any apostrophies
            playerGuess = playerGuess.replace("'","")
            
            # Replace this with nothing (remove it)
            playerGuess = playerGuess.replace("\\r\\n","")
            
            # Convert the string to an integer so we can do maths later.
            playerGuess = str(playerGuess)
            
            # Print it to see if any of that rubbish above actually worked
            print("The Player goes for", playerGuess)
            
            
            ### The Rock Paper Paper Scissors Comparison Part
            
            # Let the Computer Guess at random from 3 options
            listyMacListFace = ["rock", "paper", "scissors"]
            cpuGuess = choice(listyMacListFace)
            
            print("The computer goes for", cpuGuess)
            
            # all draws
            if playerGuess == cpuGuess:
                print("It's a draw!")
                
            # player rock
            elif playerGuess == "rock" and cpuGuess == "paper":
                print("Computer wins!")
                computerPoints = computerPoints + 1
                
            elif playerGuess == "rock" and cpuGuess == "scissors":
                print("Player wins!")
                playerPoints = playerPoints + 1
                
                
            # player paper
            elif playerGuess == "paper" and cpuGuess == "scissors":
                print("Computer wins!")
                computerPoints = computerPoints + 1
                
            elif playerGuess == "paper" and cpuGuess == "rock":
                print("Player wins!")
                playerPoints = playerPoints + 1
                
                
            # player scissors
            elif playerGuess == "scissors" and cpuGuess == "paper":
                print("Computer wins!")
                computerPoints = computerPoints + 1
                
            elif playerGuess == "scissors" and cpuGuess == "rock":
                print("Player wins!")
                playerPoints = playerPoints + 1
                
                
            print("Score: Computer:", computerPoints, "Player", playerPoints)
            print("")
        
        # Except don't try read blank numbers. Pass them by.
        except ValueError:
            pass

except KeyboardInterrupt:
    
    # https://www.youtube.com/watch?v=AxcM3nCsglA
    print("\n HE DID THE MASH! ... He did the CTRL+C mash")
    ser.close()
    print("The keyboard mash!")
    

# Don't forget you can show the show plotter on Thonny under "View"
