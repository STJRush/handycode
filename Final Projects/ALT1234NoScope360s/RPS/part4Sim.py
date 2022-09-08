
# This program takes a variable (playerGuess here but could be any serial data) from a microbit and brings it into Thonny. 
# USB Serial data comes with lots of junk text like \\r\\n so most of this program is for cleaning those parts away leaving just the variable we want.

import serial
from time import sleep
from random import choice
import pygal
import random


ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"

print("Type CTRL + C to exit. (may take 5 seconds)")

# Opens the packet of crunchie nut cornflakes
ser.open()

computerPoints = 0
playerPoints = 0

# must be one
playerRockCounter = 0
playerScissorsCounter = 0
playerPaperCounter = 0

computerRockCounter = 0
computerScissorsCounter = 0
computerPaperCounter = 0

playerRockCountSnapshot=0
playerScissorsCountSnapshot=0
playerPaperCountSnapshot=0


computerPastGuessList = []
playerPastGuessList = []


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
            #cpuGuess = choice(listyMacListFace)
            
            # mimic the player:
            cpuGuessList=(random.choices(listyMacListFace, weights=((playerRockCountSnapshot+1)**2, (playerPaperCountSnapshot+1)**2, (playerScissorsCountSnapshot+1)**2), k=20))
            print(cpuGuessList)
            cpuGuess=cpuGuessList[0]
            print("The computer goes for", "rock")
            
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
                print("Player wins!")
                
                playerPoints = playerPoints + 1
                
            elif playerGuess == "scissors" and cpuGuess == "rock":
                print("Computer wins!")
                computerPoints = computerPoints + 1
                
                        
            
            computerPastGuessList.append(cpuGuess)
            playerPastGuessList.append(playerGuess)
            
            # count how many rocks, scissors, paper the player chooses
            for guess in playerPastGuessList:
                
                if guess == "rock":
                    playerRockCounter = playerRockCounter + 1
            
                elif guess == "paper":
                    playerPaperCounter = playerPaperCounter + 1
                
                elif guess == "scissors":
                    playerScissorsCounter = playerScissorsCounter + 1
  
            playerTotalsToGraph = [playerRockCounter,playerPaperCounter,playerScissorsCounter]
        
            print("                        R  P  S")
        
            print("To Graph for player  :", playerTotalsToGraph)
            playerTotalsToGraph.sort()
            #print("The player's most common choice was guessed", playerTotalsToGraph[2], "of times")
            
            
            # Graph Player Stuff
            bar_chart = pygal.Bar(title=u'PLayer Guesses')                           
            bar_chart.add('Rock', playerRockCounter)
            bar_chart.add('Paper', playerPaperCounter)
            bar_chart.add('Scissors', playerScissorsCounter)
            bar_chart.render_to_file('player_guesses.svg') 
            

            playerRockCounter = playerRockCountSnapshot
            playerScissorsCounter = playerScissorsCountSnapshot
            playerPaperCounter = playerPaperCountSnapshot

            playerRockCounter = 0
            playerScissorsCounter = 0
            playerPaperCounter = 0
            
            # count how many rocks, scissors, paper the COMPUTER chooses
            for guess in computerPastGuessList:
                
                if guess == "rock":
                    computerRockCounter = computerRockCounter + 1
            
                elif guess == "paper":
                    computerPaperCounter = computerPaperCounter + 1
                
                elif guess == "scissors":
                    computerScissorsCounter = computerScissorsCounter + 1
                    
                    
            computerTotalsToGraph = [computerRockCounter,computerPaperCounter,computerScissorsCounter]
            
        
        
            print("To Graph for computer:", computerTotalsToGraph)
            computerTotalsToGraph.sort()
            #print("The computer's most common choice was guessed", computerTotalsToGraph[2], "of times")
            

            # Graph Player Stuff
            bar_chart = pygal.Bar(title=u'Computer Guesses')     
            bar_chart.add('Rock', computerRockCounter)
            bar_chart.add('Paper', computerPaperCounter)
            bar_chart.add('Scissors', computerScissorsCounter)
            bar_chart.render_to_file('computer_guesses.svg')        

            computerRockCounter = 0
            computerScissorsCounter = 0
            computerPaperCounter = 0  
            
            sleep(2)
        # Except don't try read blank numbers. Pass them by.
        except ValueError:
            pass

except KeyboardInterrupt:
    
    # https://www.youtube.com/watch?v=AxcM3nCsglA
    print("\n HE DID THE MASH! ... He did the CTRL+C mash")
    ser.close()
    print("The keyboard mash!")
    
