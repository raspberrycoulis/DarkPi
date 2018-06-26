![Powered by Dark Sky](https://darksky.net/dev/img/attribution/poweredby-oneline.png)

# weather-pi-data
Various Python scripts that attempt to display weather data (either via [Dark Sky](https://darksky.net/dev/) or [Open Weather Map](https://openweathermap.org/)) on various Raspberry Pi related HATs or pHATs including:

- [Display-o-Tron 3000 / HAT](https://shop.pimoroni.com/products/display-o-tron-hat)
- [Blinkt!](https://shop.pimoroni.com/products/blinkt)
- [PaPiRusZero](https://uk.pi-supply.com/products/papirus-zero-epaper-screen-phat-pi-zero)

## Requirements

- A suitable HAT or pHAT and their accompanying libraries
- [python-forecast.io](https://github.com/ZeevG/python-forecast.io)
- You'll need an API key for [Dark Sky API](https://darksky.net/dev/) or for [Open Weather Map](https://openweathermap.org/)

## Installation

Install the libraries for your HAT or pHAT:
- [Display-o-Tron 3000 / HAT](https://github.com/pimoroni/displayotron)
- [Blinkt!](https://github.com/pimoroni/blinkt)
- [PaPiRusZero](https://github.com/PiSupply/PaPiRus)

Install the required forecastio library, which is a Dark Sky API wrapper:
`sudo pip install python-forecastio`

Find your latitude and longitude [here](https://www.latlong.net/).

## Setup

For simplicity, there is a `config.ini` file inside the `config` directory. Add your Dark Sky / Open Weather Map details there.

## Additional info
### Examples - Display-o-Tron 3000

When running the `darksky-dot3k.py` script, the Display-o-Tron 3000 does a number of things:
- Displays the temperature, humidity and chance of rain in a readable format
- The backlight of the display changes colour to reflect the UV index:
    - Green = low UV index
    - Yellow = moderate UV index
    - Orange = high UV index
    - Red = very high UV index
    - Violet = extreme UV index
- The LED bar-graph will also show the chance of rain, with the more lights visible showing a higher chance
- Pressing the joystick button will exit the code and shut off the display.

### Examples - Blinkt!

The `blinkt-uvindex.py` script will pull the current UV Index and change the colour of the Blinkt accordingly:
- Green = low UV index
- Yellow = moderate UV index
- Orange = high UV index
- Red = very high UV index
- Violet = extreme UV index
It will also print out the UV index in the console. Exit with `CTRL+C` to exit cleanly. The Blinkt will be turned off.

### Examples - PaPiRus

The `darksky-papirus.py` script is similar to the Display-o-Tron 3000, except it will simply display the current weather details on the screen. Exit with `CTRL+C` which will also clear the PaPiRus after displaying a goodbye message.
