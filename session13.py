import time
import json
try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)
except PermissionError:
    print("file promission! initializing default data...")
    data = {
        "battery":{
        "min_capacity": 10,
        "max_capacity": 200
        },
        "engine_temp": {
        "MAX_TEMP": 150,
        "TEMP_RISE":5   
        }
    } 
    def smart_sensor_temp(current_temp, TEMP_INCREASE_RATE, distance_traveled, temp_محیط)
        try:

    def smart_sensor_battery(current_battery, BATTERY_DROP_RATE, current_temp, TEMP_INCREASE_RATE, distance_traveled):
        try:
            distance_factor = 1 + distance_traveled * 0.005
            new_temp = 1 + (current_temp + TEMP_INCREASE_RATE + 25) * 0.01
            new_battery = current_battery - BATTERY_DROP_RATE * new_temp * distance_factor
            return int(max(new_battery, 0))
            return int(max(new_temp, 0))
        except TypeError:
            return current_battery
