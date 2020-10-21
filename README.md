yahboom-raspi-cooling-fan
=========================

Crowd-sourced code for the "Yahboom Raspberry Pi Cooling HAT with
Intelligent Temperature Control": 

![HAT Image](yahboom-rgb-pi-hat.jpg)

This code has been tested on Raspberry Pi
OS 32-bit.

How to run the Python code
--------------------------

The code, as written by Yahboom, is for Python 2.

**Install Python 2 Packages**

```bash
sudo pip install Adafruit_BBIO Adafruit-SSD1306
```

**Run one or more of the Python scripts**

For example, if you want the Fan, RGB, and OLED all controlled
by temperature and the Pi's stats, then in three separate terminal
windows, run:

```bash
python fan_temp.py
```

```bash
python rgb_temp.py
```

```bash
python oled.py
```
