import gpiozero as GPIO
import time

# GPIO setup for solenoid switch as an output device
switch_pin = 21
sole_switch = GPIO.OutputDevice(switch_pin)

try:
  print("The solenoid is closed on startup.")
  print("ON/OFF to open/close the solenoid plunger.")

  while True:
    command = input("ON/OFF?\t").strip().upper()
    if command == "ON":
      sole_switch.on()
    elif command == "OFF":
      sole_switch.off()
    else:
      print("Enter ON/OFF please!!")
    continue

except KeyboardInterrupt:
  sole_switch.close()
