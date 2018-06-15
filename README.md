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

Put the darkypi.py script somewhere

Set the environment variables (I put them in `~/.bash_profile`)

```shell
DARKSKY_API="somethingsomething"; export DARKSKY_API
LAT="50.7"; export LAT
LON="-10.5"; export LON
```

Find your latitude and longitude [here](https://www.latlong.net/).

## Run

`python darkpi.py`

## Scheduling

We want the display to update every hour, and when we power on the device. 

I wrote a little shell script called `run.sh` to hold the environment variables because cron is... awkward

```shell
DARKSKY_API="something"; export DARKSKY_API
LAT="50.5"; export LAT
LON="-8.5"; export LON

python ~/darkpi/darkpi.py
```

Run `crontab -e` and add these entries to the crontab

```
0 * * * * /darkpi/run.sh
@reboot   /darkpi/run.sh
```
