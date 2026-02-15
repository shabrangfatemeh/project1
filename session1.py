    
sensor_readings = {"high": 70.1, "very high": 120.8, "normal": 45.7, "low": 20.4, "very low": -5}

sensor_readings["very high"] = 119
sensor_readings["melting"] = 122.5

values = list(sensor_readings.values())
total = sum(values)
mean = total / len(values)
print("updated list:", sensor_readings)
print("mean :", mean)



sensor_readings = [("high", 70.1), ("very high", 120.8), ("normal", 45.7), ("low", 20.4), ("very low", -5)]

sensor_readings.append(("melting", 122.5))
sensor_readings[2] = ("very high", 119)
values = [reading[1] for reading in sensor_readings]
total = sum(values)
mean = total / len(values)
print("updated list:", sensor_readings)
print("mean :", mean)
    
auto_status = ("move after asking the person ")
print(auto_status.upper())