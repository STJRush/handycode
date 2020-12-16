#This file will load an .mp3 music clip and a .wav sound in the same folder as itself
#You will need to download these files to run this .py file.

# You can find the files here:
# https://github.com/STJRush/Coding-Club/tree/master/pygame_Sounds

# These 3 lines of code must go at the top of your program for sounds or music to work
# You need to also install the pygame module. On the python editor Thonny, you can easily
# do this from "Tools>Manage Packages>" & search pygame, then click "install".

from pygame import mixer 
from time import sleep
mixer.init() 

# Part 1/3: HOW TO PLAY MUSIC  --------------------------------
 
# 1. Load the song. (Music files should be .mp3 files)
mixer.music.load("nextgenTheme.mp3") # This .mp3 needs to be in the same folder as your .py python file
  
# 2. Set the volume
mixer.music.set_volume(0.7) 
  
# 3. Start playing the song, allowing time (sleep in seconds) for it to play
mixer.music.play()


print("Playing music now!")
sleep(1)
print("this")
sleep(3)
print("and STOPPING")


mixer.music.stop()

sleep(1)


# Part 2/3: HOW TO PLAY SOUNDS: --------------------------------


# 1. Load in sounds ready to play later (SOUND CLIPS must be .wav or .ogg files and can NOT be .mp3)

engageSound= mixer.Sound("picard.wav") # make up a variable name eg.engageSound
makitsoSound= mixer.Sound("makitso.wav") # these sound clips must be in the same folder as your python file

print("Now playing two .wav sound clips")
sleep(1)

#plays clip
mixer.Sound.play(engageSound) 
sleep(2)

#plays clip
mixer.Sound.play(makitsoSound)
sleep(1)


# Part 3/3: HOW TO PLAY SOUND OVER SOME MUSIC --------------------------------
print("Now playing a .wav sound effect over some music")

#starts music
mixer.music.play()
sleep(2)
#plays sound clip (loaded above)
mixer.Sound.play(makitsoSound)
sleep(1)
#stops music
mixer.music.stop()

#note: Those last few lines won't work without first loading the sounds on line 44 and 45


"""
Classic mistakes along the way to getting this working:

- "No module called pygame found"

You need to install the pygame module to run this code. On the python editor "Thonny", you can easily
 do this from "Tools>Manage Packages>" & search pygame, then click "install". If you're not using
 you should google "how to install pygame in...<whatever you're using> as each program is a bit different.

 
"FileNotFoundError: No such file or directory"

a) You've not downloaded the sound into the same folder as your python file
b) You've a spelling mistake or typo in the name of your file
c) You've forgotten the file extension eg. picard instead of picard.wav


"Cannot play this sound"

You're trying play .wavs (sounds) with the code for music (.mp3) or vis versa.
mixer.Sound is for sounds and mixer.music is for music. 



"AttributeError: module 'pygame.mixer' has no attribute 'sound'"


It's pygame.Sound with a capital S, not pygame.sound with a lowercase "s".



"I get no errors but no sounds plays!!!"

- Go to youtube and search Rasputin. It's a cracking song. It'll also test your sound.

- After this, ensure you've a second or two of pause sleep(2) to allow the sound time to play.


"""








