import RPi.GPIO as GPIO
import time
import math

#Álatlános beállítások
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()


from ina219 import INA219
from ina219 import DeviceRangeError
#ina = INA219(shunt_ohms=0.1, max_expected_amps = 0.01, address=0x40)

#ina.configure(voltage_range=ina.RANGE_16V, gain=ina.GAIN_AUTO, bus_adc=ina.ADC_128SAMP, shunt_adc=ina.ADC_128SAMP)

ina = INA219(shunt_ohms=0.1)
ina.configure()

#n-re normál: [min, max] -> [0, n]
def normal(min, max,n,i):
    if(i<min):
        return 0
    else:
        return math.floor((i-min)/(max-min)*n)
    
#Méréssel meghatározzuk az áram minimális és maximális értékét
min = 0.4
max = 1.6

try:
    while True:
        u = ina.voltage()
        i = ina.current()
        p = ina.power()
        fill = normal(min, max, 100, i)
        print(f"U={u:.3f}V, I={i:.3f}mA, P={p:.3f}mW, fill={fill}%")
        #ina.sleep()
        time.sleep(1)
        #ina.wake()

except KeyboardInterrupt:
    print("Vége: Pinek leapcsolva")
    GPIO.cleanup()
