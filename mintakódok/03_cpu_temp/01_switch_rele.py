import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinSwitch = 24 # in
GPIO.setup(pinSwitch, GPIO.IN)
pinRele = 20
GPIO.setup(pinRele, GPIO.OUT)

releOnOff = True

T = 1

def venOnOff(channel):
    global releOnOff
    releOnOff = not releOnOff
    GPIO.output(pinRele, releOnOff)   

#  Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitch, GPIO.FALLING, callback=venOnOff, bouncetime=200)

try:
    while True:
        # Led fel, le       
        time.sleep(T)

    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()


