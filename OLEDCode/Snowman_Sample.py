from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
WIDTH =128 
HEIGHT= 64

i2c=I2C(1,scl=Pin(19),sda=Pin(18),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
while True:
    oled.fill(0)
    # Snowman body
    oled.ellipse(64, 48, 24, 14, 1)   # bottom circle
    oled.ellipse(64, 31, 18, 13, 1)   # middle circle
    oled.ellipse(64, 15, 12, 10, 1)   # head

    # Eyes
    oled.pixel(60, 13, 1)
    oled.pixel(68, 13, 1)
    # Nose
    oled.pixel(64, 16, 1)
    oled.pixel(65, 17, 1)
    oled.pixel(66, 18, 1)

    # Smile
    oled.pixel(59, 19, 1)
    oled.pixel(62, 21, 1)
    oled.pixel(66, 21, 1)
    oled.pixel(69, 19, 1)    
     
    # Buttons
    oled.pixel(64, 28, 1)
    oled.pixel(64, 34, 1)
    oled.pixel(64, 40, 1)

    # Hat
    oled.fill_rect(55, 2, 18, 4, 1)
    oled.fill_rect(58, 0, 12, 6, 1)

    # Arms
    oled.line(47, 30, 25, 22, 1)
    oled.line(81, 30, 103, 22, 1)   
    # Snow ground
    oled.line(0, 62, 127, 62, 1)

    # Falling snow using pixel()
    for x, y in [
        (10, 8), (25, 18), (40, 6), (90, 10),
        (110, 20), (120, 5), (15, 40), (105, 45)
    ]:
        oled.pixel(x, y, 1)
        
    oled.show()
