import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature
import board
import busio

# 7 szegmenses kijező imort
from adafruit_ht16k33 import segments
# i2c kommunikáció import
i2c = busio.I2C(board.SCL, board.SDA)
# 7 szegment kapcsoat i2c-vel
display = segments.Seg7x4(i2c)
# 7 szemg törlés
display.fill(0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinSwitch = 24 # in
GPIO.setup(pinSwitch, GPIO.IN)
pinRele = 20
GPIO.setup(pinRele, GPIO.OUT)

releOnOff = True

# cpu hőmérséklet kiolvas
def getCpuTemp():
    cpu = CPUTemperature()
    temp = cpu.temperature
    temp = round(temp, 2)
    return temp

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
        print(f"CPU: {getCpuTemp()}°C")
        temp = getCpuTemp()
        tempString = str(temp)[:5].ljust(5,"0")
        display.print(tempString)
        time.sleep(T)

    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    display.fill(0)
    GPIO.cleanup()



