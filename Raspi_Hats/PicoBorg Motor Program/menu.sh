#!/bin/bash

# GPIO assignments
DRIVE_1=4
DRIVE_2=18
DRIVE_3=8
DRIVE_4=7

# Check user ID (run as sudo if not root)
if test "$UID" -ne 0 ; then
    # We are not root, re-run as root
    echo "Not root, re-running as root"
    sudo $0
    exit 0
fi

# Set up GPIO pins as outputs
echo "$DRIVE_1" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio${DRIVE_1}/direction
echo "$DRIVE_2" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio${DRIVE_2}/direction
echo "$DRIVE_3" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio${DRIVE_3}/direction
echo "$DRIVE_4" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio${DRIVE_4}/direction

# Display the options to the user as a menu
echo "+-------------------------------+"
echo "|      PicoBorg Murray Mod      |"
echo "+-------------------------------+"
echo "|                               |"
echo "|      7              9         |"
echo "|      (@)__________(@)         |"
echo "|       |            |          |"
echo "|       |   Forward  |          |"
echo "|       |            |          |"
echo "|       |            |          |"
echo "|       |            |          |"
echo "|       |   Reverse  |          |"
echo "|      (@)__________(@)         |"
echo "|      1              3         |"
echo "|                               |"
echo "|    0      ALL STOP            |"
echo "|    Q      Quit                |"
echo "|                               |"
echo "+-------------------------------+"
echo

# Loop indefinitely
while [ 1 ]; do
    # Get the next user command
    read -sn 1 command                                      # Read the next command from the user (silent mode, 1 character)

    # Process the users command
    case "$command" in
        1)                                                  # If the user pressed 1... (rear left wheel reverse)
	    echo "0" > /sys/class/gpio/gpio${DRIVE_2}/value  # turn the opposing drive 2 off to avoid tugawar
	    echo "0" > /sys/class/gpio/gpio${DRIVE_3}/value  # turn the opposing drive 3 off to avoid tugawar
            sleep 0						# Signal time lag in seconds from Earth to Mars
	    enabled=`cat /sys/class/gpio/gpio${DRIVE_1}/value`  # Read the current state of drive 1
            if test "$enabled" -eq 0 ; then                     # If it is off...
                echo "1" > /sys/class/gpio/gpio${DRIVE_1}/value     # Turn it on
            else                                                # Otherwise...
                echo "0" > /sys/class/gpio/gpio${DRIVE_1}/value     # Turn it off
            fi            
            ;;
        7)                                                  # If the user pressed 7... (front left wheel forward)
	    echo "0" > /sys/class/gpio/gpio${DRIVE_1}/value  # turn the opposing drive 1 off to avoid tugawar
	    echo "0" > /sys/class/gpio/gpio${DRIVE_4}/value  # turn the opposing drive 4 off to avoid tugawar
            sleep 0						# Signal time lag in seconds from Earth to Mars
            enabled=`cat /sys/class/gpio/gpio${DRIVE_2}/value`  # Read the current state of drive 7
            if test "$enabled" -eq 0 ; then                     # If it is off...
                echo "1" > /sys/class/gpio/gpio${DRIVE_2}/value     # Turn it on
            else                                                # Otherwise...
                echo "0" > /sys/class/gpio/gpio${DRIVE_2}/value     # Turn it off
            fi            
            ;;
        9)                                                  # If the user pressed 9...   (front right wheel forward)
	    echo "0" > /sys/class/gpio/gpio${DRIVE_1}/value  # turn the opposing drive 1 off to avoid tugawar
	    echo "0" > /sys/class/gpio/gpio${DRIVE_4}/value  # turn the opposing drive 4 off to avoid tugawar
            sleep 0						# Signal time lag in seconds from Earth to Mars
            enabled=`cat /sys/class/gpio/gpio${DRIVE_3}/value`  # Read the current state of drive 3
            if test "$enabled" -eq 0 ; then                     # If it is off...
                echo "1" > /sys/class/gpio/gpio${DRIVE_3}/value     # Turn it on
            else                                                # Otherwise...
                echo "0" > /sys/class/gpio/gpio${DRIVE_3}/value     # Turn it off
            fi            
            ;;
        3)                                                  # If the user pressed 3...  (rear right wheel reverse)
	    echo "0" > /sys/class/gpio/gpio${DRIVE_2}/value  # turn the opposing drive 2 off to avoid tugawar
	    echo "0" > /sys/class/gpio/gpio${DRIVE_3}/value  # turn the opposing drive 3 off to avoid tugawar
            sleep 0						# Signal time lag in seconds from Earth to Mars
            enabled=`cat /sys/class/gpio/gpio${DRIVE_4}/value`  # Read the current state of drive 4
            if test "$enabled" -eq 0 ; then                     # If it is off...
                echo "1" > /sys/class/gpio/gpio${DRIVE_4}/value     # Turn it on
            else                                                # Otherwise...
                echo "0" > /sys/class/gpio/gpio${DRIVE_4}/value     # Turn it off
            fi            
            ;;
        0)                                                  # If the user pressed 0...
            # Set all drives off
            echo "0" > /sys/class/gpio/gpio${DRIVE_1}/value
            echo "0" > /sys/class/gpio/gpio${DRIVE_2}/value
            echo "0" > /sys/class/gpio/gpio${DRIVE_3}/value
            echo "0" > /sys/class/gpio/gpio${DRIVE_4}/value
            ;;
        q|Q)                                                # If the user pressed Q...
            # Release GPIO pins
            echo "$DRIVE_1" > /sys/class/gpio/unexport
            echo "$DRIVE_2" > /sys/class/gpio/unexport
            echo "$DRIVE_3" > /sys/class/gpio/unexport
            echo "$DRIVE_4" > /sys/class/gpio/unexport
            # Exit script
            exit 0                                  
            ;;
        *)                                                  # If the user pressed anything else
            echo "Unknown option '${command}'"                  # Print an error message
            ;;
    esac    
done

