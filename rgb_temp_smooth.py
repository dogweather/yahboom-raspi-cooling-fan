#
# Controls the RGB's based on the Pi's temperature. Uses an
# algorithm to compute the color dynamically.
#

import smbus
import time
import os
bus = smbus.SMBus(1)

addr = 0x0d
fan_reg = 0x08
state = 0
temp = 0
previousColor = 0
rgb_off_reg = 0x07
Max_LED = 3

RGB_COLD = (0x00, 0x00, 0xff)
RGB_HOT  = (0xFF, 0x00, 0x00)


def calculateColor(temp):
    """
    Blend COLD and HOT together using a weighted average
    technique. The weight is calculated from the temperature,
    given expected bounds of 45 and 63.
    """
    lowerBound = 45
    upperBound = 50

    bracketedTemp = min(max(lowerBound, temp), upperBound)
    percentHot    = float(bracketedTemp - lowerBound) / (upperBound - lowerBound)
    percentNot    = 1 - percentHot

    avgColor = []
    for i in (0, 1, 2):
        avgByte = int(RGB_HOT[i] * percentHot + RGB_COLD[i] * percentNot)
        avgColor.append(avgByte)

    print("Calulated average: " + avgColor.__repr__())
    
    return avgColor


def setRGB(num, r, g, b):
    if num >= Max_LED:
        bus.write_byte_data(addr, 0x00, 0xff)   # Brightness
        bus.write_byte_data(addr, 0x01, r&0xff)
        bus.write_byte_data(addr, 0x02, g&0xff)
        bus.write_byte_data(addr, 0x03, b&0xff)
    elif num >= 0:
        bus.write_byte_data(addr, 0x00, num&0xff)
        bus.write_byte_data(addr, 0x01, r&0xff)
        bus.write_byte_data(addr, 0x02, g&0xff)
        bus.write_byte_data(addr, 0x03, b&0xff)


        
bus.write_byte_data(addr,rgb_off_reg,0x00)
time.sleep(1)

while True:
    cmd = os.popen('vcgencmd measure_temp').readline()
    CPU_TEMP = cmd.replace("temp=","").replace("'C\n","")
    temp = int(float(CPU_TEMP))
    print("CPU Temperature: ", temp)
    color = calculateColor(temp)

    if color != previousColor:
        setRGB(Max_LED, color[0], color[1], color[2])
        previousColor = color

    time.sleep(.5)
    
