"""

       /,,                                                
      /\  )                                               
        \,'                                               
     /`'`\                                                
                                                          
          ,              COMMIE SENDER CODE        
         ,@,                                              
        ,@@@,            SENDS TEMPERATURE OVER SERIAL COMS       
       ,@@@@@,             
`@@@@@@@@@@@@@@@@@@@`                                     
  `@@@@@@@@@@@@@@@`                                       
DR  `@@@@@@@@@@@`                                         
   ,@@@@@@`@@@@@@,                                        
   @@@@`     `@@@@                                        
  ;@`           `@;                                       
    _   _   _   _                                         
   (   (   (   |_)                                        
    ~   ~   ~  |   

"""

# Need to read serial from a micro:bit?
# Don't want to go all the way into Makecode.org and write serial send code?
# Here's that code.

# On thonny, you can click bottom right, Python 3.7.whatever
# Change that to Micropython (BBC Micro:bit)
# Run (Choose the Micro:bit if prompted)

# If you get WARNING:root:Unexpected echo... or something like that
# Close Thonny and reopen. It just means something is running in the background.
# If you can't get past the error, paste the code into makecode.org in python
# Then swap back to blocks, download and flash to the Microbit as normal.

serial.redirect_to_usb()

def on_forever():
    basic.show_number(input.temperature())
    serial.write_line("" + str((input.temperature())))
    serial.write_line("")
basic.forever(on_forever)



