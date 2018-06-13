# weather-dot3k-darksky
An ambient weather display for Raspberry Pi Zero W, Pimoroni Display-o-Tron 3000 / HAT, and Dark Sky API

Display the weather forecast using the Dark Sky API on Pimoroni's Display-o-Tron 3000 / HAT using a Raspberry Pi. A fork of https://github.com/ideasasylum/DarkPi which uses Pimoroni's Blinkt instead.

## Requirements

- [python-forecast.io](https://github.com/ZeevG/python-forecast.io)
- [Raspberry Pi and Pimoroni's Display-o-Tron 3000 / HAT](https://shop.pimoroni.com/products/display-o-tron-hat)
- [Display-o-Tron libraries](https://github.com/pimoroni/displayotron)
- You'll need an API key for [Dark Sky API](https://darksky.net/dev/)

![Powered by Dark Sky](https://darksky.net/dev/img/attribution/poweredby-oneline.png)

## Installation

Install the Display-o-Tron libraries: https://github.com/pimoroni/displayotron
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
