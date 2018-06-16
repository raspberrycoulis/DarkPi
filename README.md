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

For simplicity, there is a `config.ini` file inside the `config` directory. Add your Dark Sky / Open Weather Map details there. **Note: Only the Dark Sky details are currently addeded here and this config will only work with the `testing.py` script until everything is up and running correctly!**