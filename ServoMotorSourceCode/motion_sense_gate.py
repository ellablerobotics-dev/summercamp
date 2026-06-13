#if motion detected, move gate
import time
from machine import I2C, Pin

from pca9685 import PCA9685

#PIR sensor pin 28
pir_sensor = Pin(28, Pin.IN)
# Initialize I2C
i2c = I2C(0, scl=Pin(17), sda=Pin(16))  # GP1 = SCL, GP0 = SDA

# Setup PCA9685
pwm = PCA9685(i2c)
servo_channel = 0  # Connect servo to PCA9685 CH0

while True:
    # Check the PIR sensor value
    if pir_sensor.value() == 0:
        print("Monitoring...")  # No motion detected
        pwm.set_servo_angle(servo_channel, 0)
    else:
        print("Somebody here!")  # Motion detected
        pwm.set_servo_angle(servo_channel, 90)
    time.sleep(1)
