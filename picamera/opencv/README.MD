# This is what worked for me:

I'm using a Raspberry Pi 4 right now with a Pi Camera 2.0

First upgradfe your pi

      sudo apt-get update
      sudo apt-get upgrade
      
Then in Terminal, intall openCV

      sudo pip install opencv-python
      
When I run this, I still get cv2 errors to do with libatlas-base-dev or something.
Basically it seems that some extra parts of this are missing. I found some code on StackOverflow that 
fixed this issue here: https://stackoverflow.com/questions/53347759/importerror-libcblas-so-3-cannot-open-shared-object-file-no-such-file-or-dire

I'll paste the code below. All this you install by typing it into the terminal:


      sudo apt-get install libcblas-dev
      sudo apt-get install libhdf5-dev
      sudo apt-get install libhdf5-serial-dev
      sudo apt-get install libatlas-base-dev
      sudo apt-get install libjasper-dev 
      sudo apt-get install libqtgui4 
      sudo apt-get install libqt4-test
  
  Then I was able to START following this tutorial here:
  
 https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
