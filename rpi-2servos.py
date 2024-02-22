# libraries needed for hardware pwm
import gpiozero as GPIO
from gpiozero.pins.pigpio import PiGPIOFactory
import time

factory = PiGPIOFactory() # setup to use PiGPIO for hardware PWM

# Setting up servo with known parameters for 0 degrees as min angle and 180 degrees as max angle
servo1_pin = 12
my_servo1 = GPIO.AngularServo(servo1_pin, initial_angle=0, min_angle=0, max_angle=180,
                             min_pulse_width=0.5/1000, max_pulse_width=2.5/1000,
                             frame_width=20/1000, pin_factory=factory)
servo2_pin = 13
my_servo2 = GPIO.AngularServo(servo2_pin, initial_angle=0, min_angle=0, max_angle=180,
                             min_pulse_width=0.5/1000, max_pulse_width=2.5/1000,
                             frame_width=20/1000, pin_factory=factory)
# Main program
try:
  print("The servos is set to 0 on startup.")
  print("SET/RESET to set the servo angle to 0/90.")

  while True:
    command = input("SET/RESET?\t").strip().upper()
    if command == "SET":
      my_servo1.angle(90)
      my_servo2.angle(90)
    elif command == "RESET":
      my_servo1.angle(0)
      my_servo2.angle(0)
    else:
      print("Enter SET/RESET please!!")

    time.sleep(1) # delay before next angle input

## Halts program when user Ctrl + C
except KeyboardInterrupt:
  my_servo1.close()
  my_servo2.close()