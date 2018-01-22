
####################################
LOAD AN IMAGE OR FILE FROM THE WEB #
####################################


import webbrowser                   # include this at the start of your program.

webbrowser.open('the_url')  # Paste your web page address instead of "the_url".

eg. 

webbrowser.open('www.google.com')  # Opens google.

################################################
LOAD AN IMAGE THAT IS ALREADY ON YOUR COMPUTER #
################################################

#You can also open a file that is offline on your computer using the browser.
#On a Windows PC, Hold down the SHIFT KEY and then Right click on the file. Choose "Copy as path".
#This will copy the address of the file; this is where it lives on your computer.
#Then paste it in as before

webbrowser.open('C:\Users\Admin\Pictures\llama.gif')  # Will give an error

#If you get a UNICODE error, double up each backslash like this:

webbrowser.open('C:\\Users\\Admin\\Pictures\\llama.gif')  # Will work


