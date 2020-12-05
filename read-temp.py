import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)


def print_gauge(name, value, text):
    print(f'# HELP {name} {text}')
    print(f'# TYPE {name} gauge')
    print(f'{name} {value}')


# the compensated_reading class has the following attributes
print_gauge("temperature", data.temperature, "Temperature in celsius")
print_gauge("pressure", data.pressure, "Pressure")
print_gauge("humidity", data.humidity, "Humidity percentage")

