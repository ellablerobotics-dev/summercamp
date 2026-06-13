#if motion detected, turn on windmill

from machine import Pin, PWM
import time

# Define the pins connected to the L298N
#FrontRightWheel
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

def move_forward(speed_percent):
    # Speed is a percentage (0 to 100), converted to 0-65535 for duty_u16
    speed_value = int(speed_percent / 100 * 65535)
    #in1.value(1) # Set direction
    #in2.value(0)
    #ena.duty_u16(speed_value) # Set speed
    FR_in1.value(0) # Set direction
    FR_in2.value(1)
    FR_ena.duty_u16(speed_value) # Set speed   
    print(f"Moving forward at {speed_percent}% speed")

def move_backward(speed_percent):
    speed_value = int(speed_percent / 100 * 65535)
    FR_in1.value(1) # Set direction
    FR_in2.value(0)
    FR_ena.duty_u16(speed_value) # Set speed
    
    print(f"Moving backward at {speed_percent}% speed")

while True:
    # Check the PIR sensor value
    if pir_sensor.value() == 0:
        print("Monitoring...")  # No motion detected
        stop_motor()
    else:
        print("Somebody here!")  # Motion detected
        try:
            move_backward(40)
        except KeyboardInterrupt:
            stop_motor() # Ensure motor stops on manual interruption
    
    time.sleep(1)



