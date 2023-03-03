import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

T = 1

pin = 18
GPIO.setup(pin, GPIO.OUT)
f = 50 # 50 Hz
fill = 100 # fill 90%
#pwm üzemmód bekapcsolása
p = GPIO.PWM(pin, f)
#indítás
p.start(fill)

try:
    while True:
        # Led fel, le       
        time.sleep(T)                        
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()

