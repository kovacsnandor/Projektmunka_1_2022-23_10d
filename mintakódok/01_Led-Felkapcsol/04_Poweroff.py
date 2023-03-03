import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinLed = 18 # out
pinSwitch = 24 # in

GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinSwitch, GPIO.IN)

print(f"Raspberry kikapcsolás. Kilép Ctrl-C")

# Eseménykezelő: lehúzásra indul
def Shutdown(channel):
    print("kikapcsolás 5 s múlva ...")
    GPIO.cleanup()
    time.sleep(5)
    os.system("sudo poweroff")
  
#  Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitch, GPIO.FALLING, callback=Shutdown, bouncetime=200)

try:
    while True:
        # Led fel, le       
        time.sleep(1)
        
        
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()



