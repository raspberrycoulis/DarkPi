#!/usr/bin/env python
# -*- coding: utf-8 -*-

from papirus import Papirus, PapirusText, PapirusTextPos
from time import sleep

from ConfigParser import ConfigParser

# Import details from config file to save typing
config = ConfigParser()
config.read('config/config.ini')
api_key = config.get('darksky', 'key')
latitude = config.get('darksky', 'latitude')
longitude = config.get('darksky', 'longitude')

try:
    import forecastio
except ImportError:
    exit("This script requires the forecastio module\nInstall with: sudo pip install forecastio")

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

screen = Papirus()
text = PapirusText()

def updateWeather():
    forecast = forecastio.load_forecast(api_key,latitude,longitude)
    temp = current.temperature
    temp = str(temp)
    humidity = current.humidity*100
    humidity = str(humidity)
    rainInt = current.precipProbability*100
    rain = str(rainInt)

try:
    screen.clear()
    print("Current weather:\nTemperture: "+temp+" °C\nHumidity: "+humidity+"%\nRain: "+rain+"%")
    text.write("Current weather:\nTemp: "+temp+" C\nHumidity: "+humidity+"%\nRain: "+rain+"%", 18)
except:
    text.write("Connection Error")
while 1:
    updateWeather()
    sleep(120)
