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
    def smart_sensor(current_battery, BATTERY_DROP_RATE, current_temp, TEMP_INCREASE_RATE, distance_traveled):
        try:
            factor_distance = 1 + distance_traveled * 0.005
            factor_temp = 1 + (current_temp + TEMP_INCREASE_RATE + 25) * 0.01
            factor_battery = current_battery - BATTERY_DROP_RATE * factor_temp *factor_distance
