#!/bin/sh
set -ex
apt-get update && apt-get -y install python3 python3-pip
pip3 install smbus2 RPi.bme280
