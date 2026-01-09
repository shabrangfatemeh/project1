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
        },
        "system_health": 100
    } 
           #  def    smart   sensor    battery   ,   temp

def smart_sensor(current_battery, BATTERY_DROP_RATE, current_temp, TEMP_INCREASE_RATE, distance_traveled, current_temp_air, REV):
        try:
            distance_factor = 1 + distance_traveled * 0.005
            REV_factor = 1 + REV * 0.003
            new_temp = 1 + (current_temp + TEMP_INCREASE_RATE + current_temp_air + REV) * 0.01
            new_battery = current_battery - BATTERY_DROP_RATE * new_temp * distance_factor
            return int(max(new_battery, new_temp, 0))
        except TypeError:
            return current_battery, current_temp
                                   #    def    WARNING!
def warning_temp_high():
    print("RED!!!")
                                      #           DEf      name   passenger
def passenger(name):
    print(f"passenger: {name}:")
                                # config
                                            #FIXED
                                 
REV = data["engine_temp"]["rev"]
TEMP_INCREASE_RATE = data["engine_temp"]["TEMP_INCREASE_RATE"]
BATTERY_DROP_RATE = data["battery"]["BATTERY_DROP_RATE"]
                                                 # variable                                                                           
rev = 100
current_temp = 40
current_battery = data["battery"]["max_capacity"]
min_battery = data["battery"]["min_capacity"]
                           # traveled
                           