import json
import time

def battery_sensor(current_battery, drop_rate):
    return current_battery - drop_rate
def temp_sensor(current_temp, rise_rate):
    return current_temp + rise_rate

try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)
    #danger not file
except FileNotFoundError:    
    print("not find! initializing default data...")
    data = {
            "engine_temp": {
            "MAX_TEMP": 200,
            "TEMP_RISE": 10
            },
            "battery": {
            "BATTERY_DROP": 5,
            "max_capacity": 100
            }
           }
# variable fixed
MAX_TEMP = data ["engine_temp"]["MAX_TEMP"]
TEMP_RISE = data ["engine_temp"]["TEMP_RISE"]
BATTERY_DROP = data["battery"]["BATTERY_DROP"]
# variable jeson
current_temp = 30
current_battery = data ["battery"]["max_capacity"]
# اجرا
passenger_car = input("what's your name?:")    
print(f"hi, welcome, {passenger_car}:")
stop_answer = input("do you have a stop on the way?(y/n): ").strip().lower()
stop_address = None
stop_distance = None 
if stop_answer in "y":
        stop_address = input("where do you want to stop?: ")
        stop_distance = int(input("distance to stop (km): "))
traveled_distance = 0   

while True:
    current_temp = temp_sensor(current_temp, TEMP_RISE)
    current_battery = battery_sensor(current_battery, BATTERY_DROP)
    traveled_distance += 1

    print(f"battery: {current_battery}")
    print(f"temp: {current_temp}")
    print(f"traveled_distance: {traveled_distance} km")

    if current_battery <= 8:
        print("battery empty")
        break   
    if stop_distance is not None and traveled_distance >= stop_distance:
        print(f"car stopped at: {stop_address}")
        break
time.sleep(1)

data ["engine_temp"]["MAX_TEMP"] = current_temp
data ["battery"]["max_capacity"] = current_battery

with open("car_report2_json", "w") as f:
    json.dump(data, f, indent=4)
print("status: save to file successfully!:") 


