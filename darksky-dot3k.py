#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dot3k import joystick as nav
from dot3k import lcd
from dot3k import backlight as backlight
backlight.use_rbg() # Required for early-batch DOT3K's as the RGB LEDs are RBG.
from time import sleep
import os
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
    
def rainWarning():
    forecast = forecastio.load_forecast(api_key,latitude,longitude)
    current = forecast.currently()
    rain = current.precipProbability*100
    if rain ==0:
        backlight.set_graph(0)
    elif (rain >1) and (rain <=9):
        backlight.set_graph(0.1)
    elif (rain >= 10) and (rain <=19):
        backlight.set_graph(0.2)
    elif (rain >= 20) and (rain <=29):
        backlight.set_graph(0.3)
    elif (rain >= 30) and (rain <=39):
        backlight.set_graph(0.4)
    elif (rain >= 40) and (rain <=49):
        backlight.set_graph(0.5)
    elif (rain >= 50) and (rain <=59):
        backlight.set_graph(0.6)
    elif (rain >= 60) and (rain <=69):
        backlight.set_graph(0.7)
    elif (rain >= 70) and (rain <=79):
        backlight.set_graph(0.8)
    elif (rain >= 80) and (rain <=89):
        backlight.set_graph(0.9)
    else:
        backlight.set_graph(1.0)

def display():
    forecast = forecastio.load_forecast(api_key,latitude,longitude)
    current = forecast.currently()
    temp = current.temperature
    temp = str(temp)
    humidity = current.humidity*100
    humidity = str(humidity)
    rain = current.precipProbability*100
    rain = str(rain)
    uvIndex = current.uvIndex
    uv = str(uvIndex)
    if uvIndex <=2.9:
        backlight.rgb(90, 148, 35)  # Green (low)
    elif (uvIndex >=3) and (uvIndex <=5.9):
        backlight.rgb(241, 227, 54) # Yellow (moderate)
    elif (uvIndex >=6) and (uvIndex <=7.9):
        backlight.rgb(217, 90, 18)  # Orange (high)
    elif (uvIndex >=8) and (uvIndex <=10.9):
        backlight.rgb(185, 2, 34)   # Red (very high)
    else:
        backlight.rgb(99, 74, 195)  # Violet (extreme)
    try:
        lcd.clear()
        lcd.set_cursor_position(0, 0)
        print("Temperture: "+temp+" C")
        lcd.write("Temp: "+temp+"\xf2C")
        lcd.set_cursor_position(0, 1)
        print("Humidity: "+humidity+"%")
        lcd.write("Humidity: "+humidity+"%")
        lcd.set_cursor_position(0, 2)
        print("Rain: "+rain+"%")
        lcd.write("Rain: "+rain+"%")
        print("UV Index: "+uv+"")
    except:
        lcd.write("Connection Error")
    
    # Press the button on the joystick to exit
    @nav.on(nav.BUTTON)
    def handle_button(pin):
        lcd.clear()
        backlight.rgb(0, 0, 0)
        backlight.set_graph(0)
        os._exit(1)

try:
    while True:
        rainWarning()
        display()
        sleep(300)  # 5 minutes
except (KeyboardInterrupt, SystemExit):
    lcd.clear()
    lcd.set_cursor_position(0, 0)
    lcd.write("Exiting...")
    lcd.set_cursor_position(0, 1)
    lcd.write("Goodbye!")
    sleep(2)
    lcd.clear()
    backlight.rgb(0, 0, 0)
    backlight.set_graph(0)
    os._exit(1)
