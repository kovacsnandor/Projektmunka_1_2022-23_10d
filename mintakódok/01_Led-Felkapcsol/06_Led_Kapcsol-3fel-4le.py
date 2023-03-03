import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinLed = 18 # out
pinSwitch = 24 # in

GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinSwitch, GPIO.IN)

onOff = False
GPIO.output(pinLed, onOff)
counter = 0
nfel = 3
nle = 4

print(f"Led kapcsolóval. Kilép Ctrl-C")

# Eseménykezelő: lehúzásra indul
def LumpOnOff(channel):
    global onOff
    global counter
    counter = counter + 1
    print(f"kapcsoltam: {counter}")
    if counter >= nfel:
        if onOff == False:
            counter = 0
            onOff = True
            GPIO.output(pinLed, onOff)
            
    if counter >= nle:
        if onOff == True:
            counter = 0
            onOff = False
            GPIO.output(pinLed, onOff)
        
    
#  Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitch, GPIO.FALLING, callback=LumpOnOff, bouncetime=200)

try:
    while True:
        # Led fel, le       
        time.sleep(1)
        
        
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()




