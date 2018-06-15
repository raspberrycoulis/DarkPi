#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dot3k import joystick as nav
from dot3k import lcd
from dot3k import backlight as backlight
backlight.use_rbg() # Required for early-batch DOT3K's as the RGB LEDs are RBG.
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

def updateWeather():
    forecast = forecastio.load_forecast(api_key,latitude,longitude)

def rainWarning():
    if rainInt <= 33:
        backlight.rgb(165, 255, 0)    # Green (good)
    elif (rainInt > 34) and (rainInt <= 74):
        backlight.rgb(226, 111, 11) # Orange (warning)
    else:
        backlight.rgb(0, 225, 255)  # Blue (you'll get wet!)

def graph():
    if rainInt ==0:
        backlight.set_graph(0)
    elif (rainInt >1) and (rainInt <=9):
        backlight.set_graph(0.1)
    elif (rainInt >= 10) and (rainInt <=19):
        backlight.set_graph(0.2)
    elif (rainInt >= 20) and (rainInt <=29):
        backlight.set_graph(0.3)
    elif (rainInt >= 30) and (rainInt <=39):
        backlight.set_graph(0.4)
    elif (rainInt >= 40) and (rainInt <=49):
        backlight.set_graph(0.5)
    elif (rainInt >= 50) and (rainInt <=59):
        backlight.set_graph(0.6)
    elif (rainInt >= 60) and (rainInt <=69):
        backlight.set_graph(0.7)
    elif (rainInt >= 70) and (rainInt <=79):
        backlight.set_graph(0.8)
    elif (rainInt >= 80) and (rainInt <=89):
        backlight.set_graph(0.9)
    else:
        backlight.set_graph(1.0)

# Press the button on the joystick to exit
@nav.on(nav.BUTTON)
def handle_button(pin):
    lcd.clear()
    backlight.rgb(0, 0, 0)
    backlight.set_graph(0)
    os._exit(1)

try:
    lcd.clear()
    lcd.set_cursor_position(0, 0)
    print("Temperture: "+temp+" °C")
    lcd.write("Temp: "+temp+" C")
    lcd.set_cursor_position(0, 1)
    print("Humidity: "+humidity+"%")
    lcd.write("Humidity: "+humidity+"%")
    lcd.set_cursor_position(0, 2)
    print("Rain: "+rain+"%")
    lcd.write("Rain: "+rain+"%")
except:
    lcd.write("Connection Error")
while 1:
    updateWeather()
    rainWarning()
    graph()
    sleep(120)