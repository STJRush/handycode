# code from Youtuber @YoungWonks
# this code turns a servo back and forth

from machine import Pin, PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 2000000

led = Pin(25, Pin.OUT)
pwm = PWM(Pin(15))

pwm.freq(50)
pwm.duty_ns(MID)

while True:
        pwm.duty_ns(MIN)
        utime.sleep(1)
        pwm.duty_ns(MID)
        utime.sleep(1)
        pwm.duty_ns(MAX)
        utime.sleep(1)
        # Raspi Pico Pinout by Danny
# Use this if you want label what pins
# you use in your code.

"""

Raspberru Pi Pico
   _______
 __[     ]__
[  [MICRO]  ]
[  [ USB ]  ]
[  [_____]  ]
[LED is GP25]
[ 0    VBUS ]     
[ 1    VSYS ] 
[ GND  GND  ] 
[ 2    3V3  ] (EN) 
[ 3    3v3  ] (OUT)
[ 4    REF  ] (ADC_VREF)
[ 5    28   ] (ADC2)
[ GND  GND  ] (AGND)
[ 6    27   ] (ADC1)
[ 7    26   ] (ADC0)
[ 8    RUN  ]
[ 9    22   ]
[ GND  GND  ]
[ 10   21   ]
[ 11   20   ]
[ 12   19   ]
[ 13   18   ]
[ GND  GND  ]
[ 14   17   ]
[ (15) 16   ]
[   o o o   ]
 -----------

"""

