#!/usr/bin/env python
# -*- coding: utf-8 -*-

from papirus import Papirus, PapirusText, PapirusTextPos
from time import sleep
import os

try:
    import forecastio
except ImportError:
    exit("This script requires the forecastio module\nInstall with: sudo pip install forecastio")

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

try:
    papirus.clear()
#    lcd.set_cursor_position(0, 0)
    print("Temperture: "+temp+" °C")
    PapirusText.write("Temp: "+temp+" C")
#    lcd.set_cursor_position(0, 1)
#    print("Humidity: "+humidity+"%")
#    lcd.write("Humidity: "+humidity+"%")
#    lcd.set_cursor_position(0, 2)
#    print("Rain: "+rain+"%")
#    lcd.write("Rain: "+rain+"%")
except:
    PapirusText.write("Connection Error")
while 1:
    updateWeather()
    sleep(120)