import time
import json
try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {
        "battery": {
            "current_level": 85,
            "BATTERY_DROP": 5,
            "CRITICAL_BATTERY": 20,
            "current_sensor_battery": 90
        }, "engine_temp": {
            "MAX_TEMP": 195,
            "TEMP_RISE": 10,
            "CRITICAL_TEMP": 200,
            "current_sensor_temp": 80
        }
    }
    # battery
CRITICAL_BATTERY = data["battery"]["CRITICAL_BATTERY"] 
BATTERY_DROP = data["battery"]["BATTERY_DROP"]
current_sensor_battery = data["battery"]["current_sensor_battery"]
    # temp
MAX_TEMP = data["engine_temp"]["MAX_TEMP"]
CRITICAL_TEMP = data["engine_temp"]["CRITICAL_TEMP"]
current_sensor_temp = data["engine_temp"]["current_sensor_temp"]
passenger = input("what's your name?:")
print(f"hi, welcom, {passenger}:")
address_passenger = input("enter the address:")
print(f"moving: {address_passenger}:")
# def battery
def status(battery):
    
while  current_sensor_battery > MAX_TEMP:
    print("EMERGENCE! STOP!")
    break
       
