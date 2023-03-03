import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinLed = 18 # out
pinSwitch = 24 # in

GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinSwitch, GPIO.IN)

# Led kigyújt
GPIO.output(pinLed, 1)

print(f"Pin világít. Kilép Ctrl-C")

try:
    while True:
        time.sleep(1)
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()


