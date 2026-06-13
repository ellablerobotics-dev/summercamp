#if motion detected, move gate
#if no motion, keep red light on
#if motion, keep green light on

import time
from machine import I2C, Pin
from pca9685 import PCA9685
from ssd1306 import SSD1306_I2C

gp1=1
gp2=2
gp3=3

ledGreenLight = Pin(gp1, Pin.OUT)
ledYellowLight = Pin(gp2, Pin.OUT)
ledRedLight = Pin(gp3, Pin.OUT)

WIDTH =128 
HEIGHT= 64

#PIR sensor pin 28
pir_sensor = Pin(28, Pin.IN)
# Initialize I2C
i2c = I2C(0, scl=Pin(17), sda=Pin(16))  # GP1 = SCL, GP0 = SDA

#olcd
i2cOLCD=I2C(1,scl=Pin(19),sda=Pin(18),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2cOLCD)


# Setup PCA9685
pwm = PCA9685(i2c)
servo_channel = 0  # Connect servo to PCA9685 CH0

while True:
    oled.fill(0)
    oled.text("Smart Farm", 0, 0)

    # Check the PIR sensor value
    if pir_sensor.value() == 0:
        print("Monitoring...")  # No motion detected
        pwm.set_servo_angle(servo_channel, 0)
        oled.text("Monitoring", 20, 30)
        ledGreenLight.off()
        ledRedLight.on()
    else:
        print("Somebody here!")  # Motion detected
        pwm.set_servo_angle(servo_channel, 90)
        oled.text("Someone here...", 20, 30)
        ledGreenLight.on()
        ledRedLight.off()
    
    oled.pixel(10,30,60)  #(x, y, color)
    oled.show()
    time.sleep(1)


