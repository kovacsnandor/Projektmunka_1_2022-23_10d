import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

T = 0.2

pinSwitch = 24 # in
GPIO.setup(pinSwitch, GPIO.IN)

class LedPWM:
    
    def __init__(self, name, pin, f, fill, delta):
        self.name = name
        self.pin = pin
        self.f = f
        self.fill = fill
        self.delta = delta
        GPIO.setup(self.pin, GPIO.OUT)
        self.p = GPIO.PWM(self.pin, self.f)
        self.p.start(self.fill)
        self.info()
        
    def info(self):
        print(f"{self.name}: f = {self.f} Hz, fill = {self.fill} %")
    
    def changeFill(self):
        self.fill += self.delta
        if self.fill>=100:
            self.fill = 100
            self.delta = - self.delta
            
        if self.fill<=0:
            self.fill = 0
            self.delta = -self.delta
        #fill frissítése
        self.p.ChangeDutyCycle(self.fill)
        self.info()
        
leds = [LedPWM("green", 18, 50, 10, 10),
        LedPWM("white", 16, 50, 50, 10),
        LedPWM("red", 21, 50, 100, 10)
        ]       

def fillUpDown(channel):
    for led in leds:
        led.changeFill()
    

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

