import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinSwitch = 24 # in
GPIO.setup(pinSwitch, GPIO.IN)
pinSwitch2 = 23 # in
GPIO.setup(pinSwitch2, GPIO.IN)

print(f"3 Led kapcsolóval (oop). Kilép Ctrl-C")

T = 0.3
auto = True

def autoOnOff(channel):
    global auto
    auto = not auto

class Led:
    def __init__(self, name, pin, nUp, nDown):
        self.name = name
        self.pin = pin
        self.nUp = nUp
        self.nDown = nDown
        self.count = 0
        self.onOff = False
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, self.onOff)
        
    def step(self):
        self.count = self.count + 1
        if self.count >= self.nUp and self.onOff == False:
            self.onOff = True
            self.count = 0
            GPIO.output(self.pin, self.onOff)
            
        if self.count >= self.nDown and self.onOff == True:
            self.onOff = False
            self.count = 0
            GPIO.output(self.pin, self.onOff)
            
        self.info()
            
    def info(self):
        print(f"{self.name}: {self.count} {self.onOff}")

# Ledek példányosítása
leds = [
    Led("Green", 18, 1,1),
    Led("White", 16, 2,2),
    Led("Red", 21, 3,3)
    ]


# Eseménykezelő: lehúzásra indul
def LedsOnOff(channel):
    for led in leds:
        led.step()
    
#  Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitch, GPIO.FALLING, callback=LedsOnOff, bouncetime=200)
GPIO.add_event_detect(pinSwitch2, GPIO.FALLING, callback=autoOnOff, bouncetime=200)

try:
    while True:
        # Led fel, le       
        time.sleep(T)
        if auto == True:
            LedsOnOff(1)
        
        
    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()





