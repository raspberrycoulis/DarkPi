#!/usr/bin/env python

from dot3k import lcd
from dot3k import backlight as backlight
backlight.use_rbg() # Required for early-batch DOT3K's as the RGB LEDs are RBG.
from time import sleep
from sys import exit

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

# Grab your API key here: http://openweathermap.org
# List of city ID city.list.json.gz can be downloaded here http://bulk.openweathermap.org/sample/
API_KEY='ADD_YOUR_API_KEY_HERE'
CITY_ID='ADD_YOUR_CITY_ID_HERE'

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
        temp = r.json().get('main').get('temp')
        humidity = r.json().get('main').get('humidity')
        print("Temperture = "+str(temp)+" C")
        lcd.write("Temperture = "+str(temp)+" C")
        sleep(5)
        lcd.clear()
        print("Humidity = "+str(humidity)+" %")
        lcd.write("Humidity = "+str(humidity)+" %")
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
