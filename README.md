# yahboom-raspi-cooling-fan

Crowd-sourced code for the "Yahboom Raspberry Pi Cooling HAT with
Intelligent Temperature Control": 

![HAT Image](yahboom-rgb-pi-hat.jpg)

I converted the code to Python 3 and tested it on
**Raspberry Pi OS 32-bit**. [attenzione](https://github.com/attenzione) tested it
successfully on **Ubuntu 64-bit** and his notes are incorporated below.


## How to run the Python code

**1. Enable I2C**

Use, for example, the [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) command line tool.

**2. Install Python3 Packages**

### Raspberry Pi OS 32-bit

```bash
sudo pip3 install Adafruit_BBIO Adafruit-SSD1306
```

### Ubuntu 64-bit

```bash
sudo apt install -y python3-smbus python3-pip python3-rpi.gpio i2c-tools libraspberrypi-bin
sudo pip3 install Adafruit-SSD1306 Pillow
```

**3. Run one or more of the Python scripts**

For example, if you want the Fan, RGB, and OLED all controlled
by temperature and the Pi's stats, then in three separate terminal
windows, run:

```bash
python3 fan_temp.py
```

```bash
python3 rgb_temp.py
```

```bash
python3 oled.py
```

### Starting a script automatically when booting

This easiest way I've found so far is to add, e.g., this line
to root's crontab with `sudo crontab -e`:

```
@reboot /usr/bin/python3 /home/pi/src/yahboom-raspi-cooling-fan/RGB_Cooling_HAT.py
```

Multiple `@reboot` lines can be given. E.g., I'm currently running these two so that
the lights simply stay default green and aren't changed:

```
@reboot /usr/bin/python3 /home/pi/src/yahboom-raspi-cooling-fan/fan_temp.py
@reboot /usr/bin/python3 /home/pi/src/yahboom-raspi-cooling-fan/oled.py
```

See Also
--------

* [Mini OLED info at Adafruit](https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage)
* [Yahboom's instructions](https://www.yahboom.net/study/RGB_Cooling_HAT)
