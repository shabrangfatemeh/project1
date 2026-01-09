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
        "TEMP_RISE":5,
        "current_temp_air": 25   
        }
    } 
           #  def    smart   sensor    battery   ,   temp

def smart_sensor(current_battery, BATTERY_DROP_RATE, current_temp, TEMP_INCREASE_RATE, distance_traveled, current_temp_air):
        try:
            distance_factor = 1 + distance_traveled * 0.005
            new_temp = 1 + (current_temp + TEMP_INCREASE_RATE + current_temp_air) * 0.01
            new_battery = current_battery - BATTERY_DROP_RATE * new_temp * distance_factor
            return int(max(new_battery, new_temp, 0))
        except TypeError:
            return current_battery, current_temp
                                   #    def    name   passenger
def             
