

```python
Raspberry Pi Pico
   _______
 __[     ]__
[  [MICRO]  ]
[  [ USB ]  ]
[  [_____]  ]
[           ]
[ 0    VBUS ]            Fantastic GPIO Pins and where to find them
[ 1    VSYS ] 
[ GND  GND  ]       <----   GND is 3rd pin down from top right near USB
[ 2    3V3  ] (EN) 
[ 3    3v3  ] (OUT) <----   +3V is 5th pin down from top right near USB
[ 4    REF  ] (ADC_VREF)
[ 5    28   ] (ADC2) <----  Analogue Input is 7th pin down from top right near USB
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
[ GND  GND  ] <----   GND is 3rd pin up on the right from the bottom of the Pico, either side.
[ 14   17   ]
[ 15   16   ] <----   GPIO16 is last pin down from top right near USB
[   o o o   ]
 -----------
```
