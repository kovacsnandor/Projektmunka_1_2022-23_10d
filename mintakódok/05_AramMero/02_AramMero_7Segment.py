import RPi.GPIO as GPIO
import time
import math

#Általános beállítások
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#---Árammérő: ina219 beállítások
from ina219 import INA219
from ina219 import DeviceRangeError
#ina = INA219(shunt_ohms=0.1, max_expected_amps = 0.01, address=0x40)

#ina.configure(voltage_range=ina.RANGE_16V, gain=ina.GAIN_AUTO, bus_adc=ina.ADC_128SAMP, shunt_adc=ina.ADC_128SAMP)

ina = INA219(shunt_ohms=0.1)
ina.configure()
#---Árammérő

#---7 szegmenses kijelző
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
# Clear the display.
display.fill(0)
#---7 szegmenses


try:
    while True:
        u = ina.voltage()
        i = ina.current()
        p = ina.power()
        fill = math.floor((i-0.4)*100/(1.6-0.4))
        print(f"U={u:.3f}V, I={i:.3f}mA, P={p:.3f}mW, fill={fill}%")
        iString = str(i)[:5].ljust(5,"0")
        display.print(iString)
        #ina.sleep()
        time.sleep(1)
        #ina.wake()

except KeyboardInterrupt:
    print("Vége: Pinek leapcsolva")
    GPIO.cleanup()
    display.fill(0)

