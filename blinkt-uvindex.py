#!/usr/bin/env python
# -*- coding: utf-8 -*-

import blinkt
from time import sleep
import sys
import os
from ConfigParser import ConfigParser

# Import details from config file to save typing
config = ConfigParser()
config.read('config/config.ini')
api_key = config.get('darksky', 'key')
latitude = config.get('darksky', 'latitude')
longitude = config.get('darksky', 'longitude')

# Blinkt stuff
blinkt.set_brightness(0.1)
blinkt.set_clear_on_exit(True)

try:
    import forecastio
except ImportError:
    exit("This script requires the forecastio module\nInstall with: sudo pip install forecastio")

def uvIndex():
    forecast = forecastio.load_forecast(api_key,latitude,longitude)
    current = forecast.currently()
    uvIndex = current.uvIndex
    try:
        if uvIndex <=2.9:
            print("The UV Index is low")
            blinkt.set_all(0, 215, 0)  # Green (low)
            blinkt.show()
        elif (uvIndex >=3) and (uvIndex <=5.9):
            print("The UV Index is moderate")
            blinkt.set_all(255, 155, 0) # Yellow (moderate)
            blinkt.show()
        elif (uvIndex >=6) and (uvIndex <=7.9):
            print("The UV Index is high!")
            blinkt.set_all(255, 35, 0)  # Orange (high)
            blinkt.show()
        elif (uvIndex >=8) and (uvIndex <=10.9):
            print("The UV Index is very high!")
            blinkt.set_all(205, 0, 0)   # Red (very high)
            blinkt.show()
        else:
            print("The UV Index is extreme!!")
            blinkt.set_all(125, 0, 225)  # Violet (extreme)
            blinkt.show()
    except:
        print("Connection Error")

try:
    while True:
        uvIndex()
        sleep(300)  # 5 minutes
except (KeyboardInterrupt, SystemExit):
    print("\nExiting...\nGoodbye!")
    sleep(2)
    sys.exit()
