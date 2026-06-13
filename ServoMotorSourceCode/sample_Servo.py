from machine import I2C, Pin
from time import sleep
from pca9685 import PCA9685

# Initialize I2C
i2c = I2C(0, scl=Pin(17), sda=Pin(16))  # GP1 = SCL, GP0 = SDA

# Setup PCA9685
pwm = PCA9685(i2c)
servo_channel = 0  # Connect servo to PCA9685 CH0

pwm.set_servo_angle(servo_channel, 90)
sleep(1)
pwm.set_servo_angle(servo_channel, 0)
sleep(1)

'''
while True:
    for angle in range(0, 90, 10):  # Sweep from 0° to 180°
        pwm.set_servo_angle(servo_channel, angle)
        print("Angle:", angle)
        sleep(0.3)

    for angle in range(180, -1, -10):  # Sweep back
        pwm.set_servo_angle(servo_channel, angle)
        print("Angle:", angle)
        sleep(0.3)
'''
