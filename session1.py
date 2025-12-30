sensor_readings = [("high", 70.1), ("very high", 120.8), ("normal", 45.7), ("low", 20.4), ("very low", -5)]

sensor_readings.append(("very high", 121.5))
sensor_readings[2] = 55

total = sum(sensor_readings)
mean = total / len(sensor_readings)
print("updated list:", sensor_readings)
print("mean :")
    
auto_status = ("move after asking the person ")
print(auto_status.upper())