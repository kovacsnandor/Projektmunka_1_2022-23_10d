import RPi.GPIO as GPIO
import time
import math
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

from ina219 import INA219
from ina219 import DeviceRangeError

ina = INA219(shunt_ohms=0.1)
ina.configure()

def normal(min, max,n,i):
    if(i<min):
        return 0
    else:
        return math.floor((i-min)/(max-min)*n)
    

print("Kilép Ctrl-C")
try:
    while True:
        u = ina.voltage()
        i = ina.current()
        p = ina.power()
        min = 0.3
        max = 0.5
        n = 101
        fill = normal(min,max,n,i)
        
        print(f"U={u:.3f}V, I={i:.3f}mA, P={p:.3f}mW, fill={fill}% Kilép Ctrl-C")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()