import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinLed = 18 # out
pinSwitch = 24 # in


GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinSwitch, GPIO.IN)

f = int(input("add meg a frekvenciát: "))
T = 1/f/2

onOff = True

print(f"Led villog: {f} Hz. Kilép Ctrl-C")

try:
    while True:
        # Led fel, le
        GPIO.output(pinLed, onOff)
        time.sleep(T)
        onOff = not onOff
        
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()

