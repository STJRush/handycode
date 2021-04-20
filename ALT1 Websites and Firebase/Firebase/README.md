# Start with "theBASICS_read_and_write_to_firebase.py"

My Read Data examples here rely people not deleting my data in the example firebase.
If silly people do delete stuff, you can re-populate it by running simTidyDataToFirebase.py above.

Things like RPi InternalTemp_write_to_csv.py or the DHT example need to Raspberry Pi to run as your PC won't have GPIO.

If want to pull down 100 points of temperture data from firebase into a csv for you to analyze, you should open the folder called "Multiple Lines and CSVs".

## THE METHOD OF NON MADNESS FOR FIREBASE

This will ensure that you're only ever 1 bug away from working, not two.

#STEP 1: 
SET UP YOUR FIREBASE ACCOUNT IN TEST MODE

#STEP 2: 
In handycode, copy paste the file simDataToFirebase.py into Thonny and run it. This will make sim data in my reposoitory which you can't see BUTUUUUUUUTT if you get no errors, very importly. your firebase and thonny is woroking which is important the next bit.

    Tips:

    - In thonny make sure you've imported the package python-firebase and installed it. NOT I REPEAT NOT one called firebase. It's python-firebase.
  
  

#STEP 3:
Change the firebase URL from my one to your one and run the code again. Now you should see a bunch of simulated data in your realtime database. Now things are really working!

#STEP 4:
Replace my code with the code from your project that generates your own data etc.
