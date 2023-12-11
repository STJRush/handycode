from pygame import mixer 
from time import sleep
mixer.init() 
mixer.music.load("nextgenTheme.mp3") # This .mp3 needs to be in the same folder as your .py python file


mixer.music.play()

print("Playing music now!")
sleep(3)

print("and STOPPING")
mixer.music.stop()

