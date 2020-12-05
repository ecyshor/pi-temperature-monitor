# pi-temperature-monitor
Raspberry pi with bme280 sensor and data output in prometheus with visualization by grafana


## Running
To run the project you have to ensure the mapped i2c device is correct (https://github.com/ecyshor/pi-temperature-monitor/blob/main/docker-compose.yml#L37).

The user owning the directory is assumed to have id 1000, if this is something else change to https://github.com/ecyshor/pi-temperature-monitor/blob/main/docker-compose.yml#L5

https://nicu.dev/posts/raspberry-pi-temperature monitor
