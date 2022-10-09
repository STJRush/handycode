from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

WIDTH  = 128                                          
HEIGHT = 64                                             

i2c = I2C(0)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    t= 27 - (reading - 0.706)/0.001721
    oled.fill(0)
    oled.text("temperature",5,5)
    oled.text(str(t),5,20)
    oled.text("C",75,20)
    oled.show() 
    utime.sleep(2)
    
    font_writer.printstring("C")
    oled.show() 
    utime.sleep(2)
    
