#!/usr/bin/env python
# -*- coding: utf-8 -*-

import blinkt
from time import sleep
import sys
import os

# Add your Dark Sky API key, latitude and longitude below

API_KEY = 'ADD-HERE'
LAT = ADD-HERE
LON = ADD-HERE

# Blinkt stuff
blinkt.set_brightness(0.1)
blinkt.set_clear_on_exit(True)

try:
    import darksky
except ImportError:
    exit("This script requires the forecastio module\nInstall with: git clone https://github.com/raspberrycoulis/dark-sky-python.git\nThen run sudo python setup.py install in the directory")

def rain():
    f = darksky.Forecast(API_KEY, LAT, LON)
    hourly = f.hourly
    rain = hourly[1].precipProbability*100
    try:
        if rain <=19:
            print("The chance of rain is very low")
            blinkt.set_all(0, 215, 0)  # Green ( very low)
            blinkt.show()
        elif (rain >=20) and (rain <=39):
            print("The chance of rain is low")
            blinkt.set_all(255, 155, 0) # Yellow (low)
            blinkt.show()
        elif (rain >=40) and (rain <=59):
            print("The chance of rain is moderate!")
            blinkt.set_all(255, 35, 0)  # Orange (moderate)
            blinkt.show()
        elif (rain >=60) and (rain <=79):
            print("The chance of rain is very high!\nDon't forget your umbrella!")
            blinkt.set_all(205, 0, 0)   # Red (high)
            blinkt.show()
        else:
            print("The chance of rain is extreme!\nIt's probably raining now!")
            blinkt.set_all(0, 10, 255)  # Blue (extreme)
            blinkt.show()
    except:
        print("Connection Error")

try:
    while True:
        rain()
        sleep(300)  # 5 minutes
except (KeyboardInterrupt, SystemExit):
    print("\nExiting...\nGoodbye!")
    sleep(2)
    sys.exit()
