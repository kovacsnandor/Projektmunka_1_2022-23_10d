import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

T = 0.2

pinSwitch = 24 # in
GPIO.setup(pinSwitch, GPIO.IN)

pin = 18
GPIO.setup(pin, GPIO.OUT)
f = 50 # 50 Hz
fill = 10 # fill 90%
delta = 10
#pwm üzemmód bekapcsolása
p = GPIO.PWM(pin, f)
#indítás
p.start(fill)
print(f"f = {f} Hz, fill = {fill} %")

def fillUpDown(channel):
    global fill
    global delta
    fill += delta
    if fill>=100:
        fill = 100
        delta = - delta
        
    if fill<=0:
        fill = 0
        delta = -delta
    #fill frissítése
    p.ChangeDutyCycle(fill)
    print(f"f = {f} Hz, fill = {fill} %")
    

#  Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitch, GPIO.FALLING, callback=fillUpDown, bouncetime=200)

try:
    while True:
        # Led fel, le       
        time.sleep(T)
        if GPIO.input(pinSwitch) == 0:
            fillUpDown(1)
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
