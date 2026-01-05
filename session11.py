import time
import json
try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {
        "battery": {
            "min_capacity": 15,
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
min_capacity = data["battery"]["min_capacity"]    
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
# def 
def show_status(battery):
    return current_sensor_battery - 5
def show_status(temp):
    return current_sensor_temp - 10 
while true:
    battery = current_sensor_battery
    engine_temp = current_sensor_temp
    if current_sensor_battery < min_capacity:
        print("please STOP!")
        break
    if current_sensor_temp >  CRITICAL_TEMP: 
        print("EMERGENCE! stope!")
        break
    choes1 = input("Are you stopping along the way?(y/n): ")
    if choes1 == "y":
       print("where do you stop?: ")
      
data["battery"]["min_capacity"] = min_capacity
data["battery"]["CRITICAL_BATTERY"] = CRITICAL_BATTERY
data["battery"]["BATTERY_DROP"] = BATTERY_DROP
data["battery"]["current_sensor_battery"] = current_sensor_battery
data["engine_temp"]["MAX_TEMP"] = MAX_TEMP
data["engine_temp"]["CRITICAL_TEMP"] = CRITICAL_TEMP
data["engine_temp"]["current_sensor_temp"] = current_sensor_temp
 
with open("car_report2_json", "w") as f:
    json.dump(data, f,indent=4)
     