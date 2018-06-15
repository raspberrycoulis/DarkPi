#!/usr/bin/env python
# -*- coding: utf-8 -*-

import forecastio
from dot3k import lcd
from dot3k import backlight as backlight
backlight.use_rbg() # Required for early-batch DOT3K's as the RGB LEDs are RBG.
from time import sleep
from sys import exit

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

# Grab your API key here: https://darksky.net/dev/
# Find your latitude and longitude here https://www.latlong.net/
api_key = 'ADD_YOUR_API_KEY_HERE'
latitude = 'ADD_YOUR_LATITUDE_HERE'
longitude = 'ADD_YOUR_LONGITUDE_HERE'

city = 'ADD_YOUR_CITY_HERE'

forecast = forecastio.load_forecast(api_key,latitude,longitude)
current = forecast.currently()
daily = forecast.daily()


try:
    lcd.set_cursor_position(0, 0)
    print("City: "+str(city)+" ")
    lcd.write("City: "+str(location)+" ")
    lcd.set_cursor_position(0, 1)
    print("Temperture: "+str(current.temperature)+" °C")
    lcd.write("Temp: "+str(current.temperature)+" °C")
    lcd.set_cursor_position(0, 2)
    print("Humidity: "+str(current.humidity)+" %")
    lcd.write("Humidity: "+str(current.humidity)+" %")
except:
    lcd.write("Connection Error")
while 1:
    forecast
    sleep(120)
    lcd.clear()