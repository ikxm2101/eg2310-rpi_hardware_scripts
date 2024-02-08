# libraries needed for hardware pwm
import gpiozero as GPIO
from gpiozero.pins.pigpio import PiGPIOFactory
import time

factory = PiGPIOFactory() # setup to use PiGPIO for hardware PWM

# Setting up servo with known parameters for 0 degrees as min angle and 180 degrees as max angle
servo_pin = 12
my_servo = GPIO.AngularServo(servo_pin, initial_angle=90, min_angle=0, max_angle=180,
                             min_pulse_width=0.5/1000, max_pulse_width=2.5/1000,
                             frame_width=20/1000, pin_factory=factory)
# Main program
try:
  print("Only works for integer values.")
  ## Main loop
  while True:
    angle = input("Enter an angle between 0 to 180 in degrees: ").strip()
    if (not angle.isdigit()) or (int(angle) < 0) or (int(angle) > 180): # checks if input is an integer input between 0 to 180
      print("Enter an integer value between 0 to 180!")
      continue
    
    print("Angle: ", angle) # statement to feedback angle to user
    my_servo.angle=int(angle) # rotate servo to angle specified by user

    time.sleep(1) # delay before next angle input

## Halts program when user Ctrl + C
except KeyboardInterrupt:
  my_servo.stop()
  GPIO.cleanup()