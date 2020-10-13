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
level_temp = 0
rgb_off_reg = 0x07
Max_LED = 3

RGB_COLD = (0x00, 0x00, 0xff)
RGB_HOT  = (0xFF, 0x00, 0x00)


def calculateColor(temp):
    return RGB_HOT


def setRGB(num, r, g, b):
    if num >= Max_LED:
        bus.write_byte_data(addr, 0x00, 0xff)
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
    print(CPU_TEMP)
    temp = float(CPU_TEMP)

    if abs(temp - level_temp) >= 1:
        color = calculateColor(temp)
        setRGB(Max_LED, color[0], color[1], color[2])
        
        if temp <= 45:
            level_temp = 45
        elif temp >= 63:
            level_temp = 63
        else:
            level_temp = temp

    time.sleep(.5)
    
