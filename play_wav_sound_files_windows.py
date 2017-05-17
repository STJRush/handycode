import pyglet #this needs to be installed on the PC by Admin*

music = pyglet.resource.media("limit.wav")  # sound file must be in same folder as 
music.play()                                # the your python file. Mp3 may not work.
pyglet.app.run()


# To install on your computer, hold the windows key and hit "R". Type "cmd" to
# bring up command. Then type "sudo pip install pyglet". It will download and install.
