# followed tutorial at https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico
# installed micropython-ssd1306
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

oled = SSD1306_I2C(128, 32, i2c) # set you oled size, mine was 128 pixels x 32 pixels

oled.text("HI DANNY", 0, 0)
oled.hline(2,31,120,1)
oled.show()