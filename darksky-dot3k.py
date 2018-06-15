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

# Get the forecast details from Dark Sky
forecast = forecastio.load_forecast(api_key,latitude,longitude)
current = forecast.currently()

# Get the temperature, humidity and chance of rain then
# convert to strings to display on DOT3K.
temp = current.temperature
temp = str(temp)
humidity = current.humidity*100
humidity = str(humidity)
rainInt = current.precipProbability*100
rain = str(rainInt)

def rainWarning():
    if rainInt <= 10:
        backlight.rgb(0, 255, 0)
    elif (rainInt > 11) and (rainInt <= 74):
        backlight.rgb(255, 0, 0)
    else:
        backlight.rgb(0, 0, 255)

try:
    lcd.set_cursor_position(0, 0)
    print("Temperture: "+temp+" °C")
    lcd.write("Temp: "+temp+" C")
    lcd.set_cursor_position(0, 1)
    print("Humidity: "+humidity+" %")
    lcd.write("Humidity: "+humidity+" %")
    lcd.set_cursor_position(0, 2)
    print("Rain: "+rain+" %")
    lcd.write("Rain: "+rain+" %")
except:
    lcd.write("Connection Error")
while 1:
    forecast
    rainWarning()
    sleep(120)
    lcd.clear()