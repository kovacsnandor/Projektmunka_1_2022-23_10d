import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinLed = 18 # out
pinSwitch = 24 # in

GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinSwitch, GPIO.IN)

onOff = True

print(f"Led kapcsolóval. Kilép Ctrl-C")

# Eseménykezelő: lehúzásra indul
def LumpOnOff(channel):
    global onOff
    print("kapcsoltam")
    GPIO.output(pinLed, onOff)
    onOff = not onOff
    
#  Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitch, GPIO.FALLING, callback=LumpOnOff, bouncetime=200)

try:
    while True:
        # Led fel, le       
        time.sleep(1)
        
        
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()


