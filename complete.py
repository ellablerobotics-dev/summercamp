#if motion detected, move gate
import time
from machine import I2C, Pin, PWM
from pca9685 import PCA9685
from ssd1306 import SSD1306_I2C
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

# setup for windmill
# Define the pins connected to the L298N
FR_ENA_PIN = 6
FR_IN1_PIN = 7
FR_IN2_PIN = 8

#PIR sensor pin 28
pir_sensor = Pin(28, Pin.IN)

# Initialize the pins as output
FR_in1 = Pin(FR_IN1_PIN, Pin.OUT)
FR_in2 = Pin(FR_IN2_PIN, Pin.OUT)
FR_ena = PWM(Pin(FR_ENA_PIN))


# Configure PWM frequency (e.g., 1000 Hz)
FR_ena.freq(1000)

def stop_motor():
    FR_in1.value(0)
    FR_in2.value(0)
    FR_ena.duty_u16(0) # Stop the motor
    
    print("Motor stopped")

def move_motor(speed_percent):
    # Speed is a percentage (0 to 100), converted to 0-65535 for duty_u16
    speed_value = int(speed_percent / 100 * 65535)

    FR_in1.value(0) # Set direction
    FR_in2.value(1)
    FR_ena.duty_u16(speed_value) # Set speed   
    print(f"Moving forward at {speed_percent}% speed")


while True:
    oled.fill(0)
    oled.text("Smart Farm", 0, 0)

    # Check the PIR sensor value
    if pir_sensor.value() == 0:
        print("Monitoring...")  # No motion detected
        pwm.set_servo_angle(servo_channel, 0)
        oled.text("Monitoring", 20, 30)
        stop_motor()
    else:
        print("Somebody here!")  # Motion detected
        pwm.set_servo_angle(servo_channel, 90)
        oled.text("Someone here...", 20, 30)
        move_motor(50)
    
    oled.pixel(10,30,60)  #(x, y, color)
    oled.show()
    time.sleep(1)


