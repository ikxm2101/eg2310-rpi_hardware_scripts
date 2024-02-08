# EG2310
# This code is used to control the servo
# Students will be given this code but will need to understand how it works
# Additional h/w exercise is to write a function to turn the servo by an angle
# The servo motor may be chosen to tilt the payload

import time
import RPi.GPIO as GPIO

# Function to map angle to PWM duty cycle for the servo
def angle_to_dutycycle(angle: int) -> float:
  """
  Duty(%) | Angle (degrees)
  2.5       0
  7.5       90
  12.5      180

  Assume linear relationship, Duty = m*Angle + c -> Duty = (5/90)*Angle + 2.5
  """
  return (5/90)*angle + 2.5

# GPIO setup for servo
## Set pin numbering convention
GPIO.setmode(GPIO.BCM)

## Choose an appropriate pwm channel to be used to control the servo
servo_pin = 12

## Set the pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

## Initialise the servo to be controlled by PWM with 50 Hz frequency (20 ms pulse length)
my_servo = GPIO.PWM(servo_pin, 50)

## Set servo to 90 degrees as it's starting position
my_servo.start(7.5)

# Main program
try:
  print("Only works for integer values.")

  ## Main loop
  while True:
    angle = input("Enter an angle between 0 to 180 in degrees: ").strip()
    if (not angle.isdigit()) or (int(angle) < 0) or (int(angle) > 180): # checks if input is an integer input between 0 to 180
      print("Enter an integer value between 0 to 180!")
      continue

    duty_cycle = angle_to_dutycycle(int(angle))
    print("Angle: ", angle, "Duty Cycle: ", duty_cycle) # statement to feedback angle and duty cycle to user
    my_servo.ChangeDutyCycle(duty_cycle) # change duty cycle to the calculated duty cycle based on angle input

    time.sleep(1) # delay before next angle input

## Halts program when user Ctrl + C
except KeyboardInterrupt:
  my_servo.stop()
  GPIO.cleanup()