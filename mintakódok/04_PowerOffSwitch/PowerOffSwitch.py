import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

pin = 40
GPIO.setup(pin, GPIO.IN)

# Our function on what to do when the button is pressed

def Shutdown(channel):
    print("Shutting Down")
    #time.sleep(5)
    #os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens

#GPIO.add_event_detect(pin, GPIO.RISING, callback=Shutdown, bouncetime=1000)
#GPIO.add_event_detect(pin, GPIO.FALLING, callback=Shutdown, bouncetime=2000)
GPIO.add_event_detect(pin, GPIO.BOTH, callback=Shutdown, bouncetime=500)


# Now wait!
try:
    while 1:
        time.sleep(1)
    
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()    
    