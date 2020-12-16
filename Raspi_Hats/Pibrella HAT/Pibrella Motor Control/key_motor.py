import pibrella
import time

weight = float(input("blah0"))

try:
    while true:
        if weight ==1:
            pibrella.output.e.on()
            weight = float(input("blah1"))
        elif weight ==1:
            pibrella.output.e.on()
            weight = float(input("blah2"))
        else:
            weight = float(input("blah3"))

except KeyboardInterrupt:
    #Ctrl + c will turn off the motors safely
    print "And we're done here"