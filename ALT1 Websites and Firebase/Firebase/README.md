# Start with "theBASICS_read_and_write_to_firebase.py"

My Read Data examples here rely people not deleting my data in the example firebase.
If silly people do delete stuff, you can re-populate it by running simTidyDataToFirebase.py above.

Things like RPi InternalTemp_write_to_csv.py or the DHT example need to Raspberry Pi to run as your PC won't have GPIO.

If want to pull down 100 points of temperture data from firebase into a csv for you to analyze, you should open the folder called "Multiple Lines and CSVs".

## THE METHOD OF NON-MADNESS FOR FIREBASE

This will ensure that you're only ever 1 bug away from working, not two.

# STEP 1: 
SET UP YOUR FIREBASE ACCOUNT IN TEST MODE

-Sign up with your google account
-Create a Realtime Database
-Set it to test mode

If you're stuck... here's a blog post I wrote the first time I setup firebase and got it running
https://docs.google.com/document/d/11mXCblg5Osas-MobqXqqu5gvMX5BdV-sG4j6_8Osugg/edit#heading=h.roclnu7xe40s

# STEP 2: 

In Thonny, go into [Tools > Manage Packages] and search for <b>python-firebase</b> . Click install.

In handycode, copy paste the file "simDataToFirebase.py" into Thonny and run it. This will make sim data in my repo which you can't see BUTUUUUUUUTT if you get no errors, very importly. your firebase and thonny is working which is important the next bit.

    Tips:

    - In thonny make sure you've imported the package python-firebase and installed it. NOT I REPEAT NOT one called firebase. It's python-firebase.
    - If you get an async error, you need to watch the video below which has instructions on how to fix it
    - If you're other errors on your Raspberry Pi try running sudo apt-get update and sudo apt-get upgrade on you Pi's terminal.
  
  

# STEP 3:
Change the firebase URL (https://cookietest-a4f79.firebaseio.com) from my one here to your one which you can find on your firebase dashboard and run the code again. Now you should see a bunch of simulated data in your realtime database. Now things are really working!

![Image of Firebasesessss](https://github.com/STJRush/handycode/blob/master/ALT1%20Websites%20and%20Firebase/Firebase/firebasetips.PNG)



# STEP 4:
Replace my code with the code from your project that generates your own data etc.

[![If you get stuck, there's a video of Firebase Errors here:](https://lh3.googleusercontent.com/proxy/8bHpJERKz6suTVBLn5QBYW8lGaBHmqsGgsQhoRmQogEWrW9oGVhljGyP4mzNUmnAOMTZPmnq2R6BCR2i0cv-WiKv6wJWofpijlB-t4HfWENGmnXkTjYHlOEIQbYiBShFG6iWo0jQtw2AettRXFs)](https://www.youtube.com/embed/o8UChpqV8Ow)

