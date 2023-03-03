import time

# Import all board pins.
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
# Or this creates a 14 segment alphanumeric 4 character display:
# display = segments.Seg14x4(i2c)
# Or this creates a big 7 segment 4 character display
# display = segments.BigSeg7x4(i2c)
# Finally you can optionally specify a custom I2C address of the HT16k33 like:
# display = segments.Seg7x4(i2c, address=0x70)

# Clear the display.
display.fill(0)

# Can just print a number
number = 0.03
numberString = str(number)[:5].ljust(5,"0")
display.print(numberString)
time.sleep(2)
numberString = "ABCD".ljust(4," ")
display.print(numberString)
time.sleep(2)
numberString = "EF".ljust(4," ")
display.print(numberString)

display.print(numberString)
time.sleep(2)
display.fill(0)
