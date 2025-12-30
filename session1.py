sensor_readings = [("high", 70.1), ("very high", 120.8), ("normal", 45.7), ("low", 20.4), ("very low", -5)]

sensor_readings.append(("melting", 122.5))
sensor_readings[2] = ("normal", 55)
values = [reading[1] for reading in sensor_readings]
total = sum(values)
mean = total / len(values)
print("updated list:", sensor_readings)
print("mean :")
    
auto_status = ("move after asking the person ")
print(auto_status.upper())