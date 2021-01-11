# WTF are keys and values?

It's cool! You know this. They're the same as Names and Values. Like:

    <i>Name : Value</i>

    DannysAge : 99

    BennysAge : 101


And from for example... a firebase database for your sensor


    Temperature : 23      # Temperature is the Key, 23 is the value

    Temperature : 24      # Temperature is the Key, 24 is the value

Python has a data type that's not a list or integer called a dictionary.
This is basically a database just like Firebase or a csv file.
It calls Names "keys". Go figure. Values are still values. Yay.

# WTF are you telling me this for?

Because you're about to try read an integer or a list from your firebase and you'll weep tears
of confusion when nothing works. They get downloaded as a dictionary data type. Your normal
attacks won't work on these enemies. You've got pluck out the "Value" using something like
a for loop (see the code above). 

    # this is a dictionary (a python database datatype so we need to pull out values into a list)
    for x in fireBDatas: # go through the dictionary of keys and values eg. Temp(key):53(value)

      print(x) # print out the key
      print(fireBDatas[x]) # print out just the value
