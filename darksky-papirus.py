#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script will get the current weather forecast from     #
# Dark Sky and display a variety of stats on PiSupply's      #
# PaPiRus, including temperature, humidity, and the chance   #
# of rain.                                                   #
# Created by Wesley Archer (@raspberrycoulis)                #

import os
from papirus import Papirus, PapirusText, PapirusTextPos
from time import sleep

from ConfigParser import ConfigParser

# Import details from config file to save typing
config = ConfigParser()
config.read('config/config.ini')
api_key = config.get('darksky', 'key')
latitude = config.get('darksky', 'latitude')
longitude = config.get('darksky', 'longitude')
units = config.get('darksky', 'units')

# For PaPiRus
screen = Papirus()
text = PapirusText()

try:
    import darksky
except ImportError:
    exit("This script requires the Dark Sky Python API Wrapper\nInstall with: git clone https://github.com/raspberrycoulis/dark-sky-python.git\nThen run sudo python setup.py install in the directory")

def display():
    forecast = darksky.Forecast(api_key, latitude, longitude, units=units)
    current = forecast.currently
    temp = current.temperature
    temp = str(temp)
    humidity = current.humidity*100
    humidity = str(humidity)
    rain = current.precipProbability*100
    rain = str(rain)
    try:
        screen.clear()
        print("Current weather:\nTemperture: "+temp+" C\nHumidity: "+humidity+"%\nRain: "+rain+"%")
        text.write("Current weather:\nTemp: "+temp+" C\nHumidity: "+humidity+"%\nRain: "+rain+"%")
    except:
        text.write("Connection Error!")

try:
    while True:
        display()
        sleep(300)  # 5 minutes
except (KeyboardInterrupt, SystemExit):
    screen.clear()
    text.write("Exiting...\nGoodbye!")
    sleep(2)
    screen.clear()
    os._exit(1)
