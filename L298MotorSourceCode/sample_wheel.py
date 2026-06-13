from machine import Pin, PWM
import time

# Define the pins connected to the L298N
FR_ENA_PIN = 6
FR_IN1_PIN = 7
FR_IN2_PIN = 8


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
    speed_value = int(speed_percent / 100 * 65535)
    FR_in1.value(1) # Set direction
    FR_in2.value(0)
    FR_ena.duty_u16(speed_value) # Set speed
    
    print(f"Moving backward at {speed_percent}% speed")

# Main test sequence
try:

    move_motor(50)
    time.sleep(5) # Run backward for 3 seconds

    stop_motor()

except KeyboardInterrupt:
    stop_motor() # Ensure motor stops on manual interruption


