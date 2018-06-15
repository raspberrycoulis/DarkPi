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
units = 'auto'

city = 'ADD_YOUR_CITY_HERE'

forecast = forecastio.load_forecast(api_key,latitude,longitude,units)
current = forecast.currently()
daily = forecast.daily()

print current
print daily

#try:
#    location = city
#    temp = r.json().get('currently').get('temp')
#    humidity = r.json().get('main').get('humidity')
#    lcd.set_cursor_position(0, 0)
#    print("City: "+str(location)+" ")
#    lcd.write("City: "+str(location)+" ")
#    lcd.set_cursor_position(0, 1)
#    print("Temperture: "+str(temp)+" °C")
#    lcd.write("Temp: "+str(temp)+" °C")
#    lcd.set_cursor_position(0, 2)
#    print("Humidity: "+str(humidity)+" %")
#    lcd.write("Humidity: "+str(humidity)+" %")
#except:
#    lcd.write("Connection Error")

#while 1:
#    forecast
#    sleep(120)
#    lcd.clear()