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

def venOnOff(channel):
    global releOnOff
    releOnOff = not releOnOff
    GPIO.output(pinRele, releOnOff) 

#  Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitch, GPIO.FALLING, callback=venOnOff, bouncetime=200)

T = 0.5
n = 20
counter = 0
x = getCpuTemp()
list = [x]*n
min = x
max = x
tMin = 45
tMax = 45.3

def avgTemp(temp):
    global counter
    global max
    global min
    index = counter % len(list)
    list[index] = temp
    tempAvg = sum(list)/len(list)
    tempAvg = round(tempAvg,2)
    counter = counter + 1
    if tempAvg > max:
        max = tempAvg
    if tempAvg < min:
        min = tempAvg
    if tempAvg > tMax:
        #ventillátor be
        GPIO.output(pinRele, 0)
    if tempAvg < tMin:
        # vent ki
        GPIO.output(pinRele, 1)
    
    
    return tempAvg


try:
    while True:
        # Led fel, le       
        temp = getCpuTemp()
        aT = avgTemp(temp)
        print(f"CPU:{temp}°C, avg:{aT}°C, min:{min}°C, max:{max}°C, {list}")
        tempString = str(aT)[:5].ljust(5,"0")
        display.print(tempString)
        time.sleep(T)

    
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    display.fill(0)
    GPIO.cleanup()




