#Method 1 Plays .wav files only

import winsound

winsound.PlaySound('typeyoursoundfilename.wav', winsound.SND_FILENAME)

# If you only have an mp3, try this: http://audio.online-convert.com/convert-to-wav
# Or just get all the awesome .wav sound files at http://www.wavsource.com/




#Method 2 Can play .wavs and some .mp3 files but THIS MODULE MUST BE INSTALLED ON THE COMPUTER BY ADMIN

import pyglet 

music = pyglet.resource.media("typeyoursoundfilename.wav")  # sound file must be in same folder as 
music.play()                                                # the your python file. Mp3 may not work.
pyglet.app.run()


# To install on your computer, hold the windows key and hit "R". Type "cmd" to
# bring up command. Then type "sudo pip install pyglet". It will download and install.
