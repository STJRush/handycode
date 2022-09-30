
# Part 4a (Upload Name and Top Score to a Website)
# Part 4b  
import serial
from time import sleep
import pygal
from random import choices
import sys 
from urllib.request import urlopen




ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM7"

myAPI = "JDB150GBC7UT6MG7"  #your key from your own thingspeak account. Put yours here.

print("Type CTRL + C to exit. (may take 5 seconds)")


def updateThingSpeak(): 
   print('Now updating thingspeak') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI    

   f = urlopen(baseURL + "&field1=%s" % ("Danny") + "&field2=%s" % (finalScore) ) 
   print ("Success! I uploaded data point No. ", f.read())
   f.close()


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

#NEW#  Declare these
playerRockCountSnapshot=0
playerScissorsCountSnapshot=0
playerPaperCountSnapshot=0


computerPastGuessList = []
playerPastGuessList = []


# Try this unless you hit CTL+C
try:
    
    # In fact... keep trying it! Again and again! MOAR!
    for plays in range(3):
        
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
            
            #weigthtedGuesses=choices(nameOfList, weights=(1, 0, 100), k=10)
            
            # mimic the player with weighted choices
            cpuGuessList=(choices(listyMacListFace, weights=((playerRockCountSnapshot+1), (playerPaperCountSnapshot+1), (playerScissorsCountSnapshot+1)), k=34))
            cpuGuess=cpuGuessList[0]
            

            #NEW# now that you can mimic, switch to the opposite pattern to counter
            if cpuGuess == "paper":
                cpuGuess = "scissors"
            elif cpuGuess == "scissors":
                cpuGuess = "rock"
            elif cpuGuess == "rock":
                cpuGuess = "paper"

            
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
                
                        
            # add the guesses eg. rock, paper to a big past list of all their guesses
            computerPastGuessList.append(cpuGuess)
            playerPastGuessList.append(playerGuess)
            
            # count how many rocks, scissors, paper the player has choosen
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
            
            #NEW# save a snapshot of the barchart scores before the couters are reset
            playerRockCountSnapshot = playerRockCounter
            playerScissorsCountSnapshot = playerScissorsCounter
            playerPaperCountSnapshot = playerPaperCounter

            # reset the counters to start count at 0 instead of counting 1,12,123,1234,12345
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
            
            
            sleep(1)
            print("Scores: Player",playerPoints,"Computer:", computerPoints)
            
            
        # Except don't try read blank numbers. Pass them by.
        except ValueError:
            pass
        
    finalScore = playerPoints - computerPoints
    print("Final Score is...", finalScore)
    updateThingSpeak()

except KeyboardInterrupt:
    
    # https://www.youtube.com/watch?v=AxcM3nCsglA
    print("\n HE DID THE MASH! ... He did the CTRL+C mash")
    ser.close()
    print("The keyboard mash!")
    
