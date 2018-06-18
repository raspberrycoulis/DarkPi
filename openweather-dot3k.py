#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dot3k import lcd
from dot3k import backlight as backlight
backlight.use_rbg() # Required for early-batch DOT3K's as the RGB LEDs are RBG.
from time import sleep
from sys import exit
from ConfigParser import ConfigParser

# Import details from config file to save typing
config = ConfigParser()
config.read('config/config.ini')
API_KEY = config.get('openweather', 'key')
CITY_ID = config.get('openweather', 'city')

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

url = 'http://api.openweathermap.org/data/2.5/weather'

temp = 0

def update_weather():
    payload = {
        'id': CITY_ID,
        'units': 'metric',
        'appid': API_KEY
    }
    global temp
    try:
        r = requests.get(url=url, params=payload)
        location = r.json().get('name')
        temp = r.json().get('main').get('temp')
        humidity = r.json().get('main').get('humidity')
        lcd.set_cursor_position(0, 0)
        print("City: "+str(location)+" ")
        lcd.write("City: "+str(location)+" ")
        lcd.set_cursor_position(0, 1)
        print("Temperture: "+str(temp)+" °C")
        lcd.write("Temp: "+str(temp)+" °C")
        lcd.set_cursor_position(0, 2)
        print("Humidity: "+str(humidity)+" %")
        lcd.write("Humidity: "+str(humidity)+" %")
    except:
        lcd.write("Connection Error")

#def show_graph(v, r, g, b):
#    v *= blinkt.NUM_PIXELS
#    for x in range(blinkt.NUM_PIXELS):
#        if v < 0:
#            r, g, b = 0, 0, 0
#        else:
#            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
#        blinkt.set_pixel(x, r, g, b)
#        v -= 1
#    blinkt.show()

#def draw_thermo(temp):
#    v = temp
#    v /= 40
#    v += (1/8)
#    show_graph(v, 255, 0, 0)

#blinkt.set_brightness(0.1)

while 1:
    update_weather()
#    draw_thermo(temp)
    sleep(120)
    lcd.clear()
