import json
import time

def battery_sensor(current_battery, drop_rate):
    return current_battery - drop_rate
def temp_sensor(current_temp, rise_rate):
    return current_temp - rise_rate

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

while True:
    current_temp = temp_sensor(current_temp, TEMP_RISE)
    current_battery = battery_sensor(current_battery, BATTERY_DROP)

    print(f"status current_battery: {current_battery}")
    print(f"status current_temp: {current_temp}")

    if current_battery <= 8:
        print("battery empty")
        break   
time.sleep(1)

data ["engine_temp"]["MAX_TEMP"] = current_temp
data ["battery"]["max_capacity"] = current_battery

with open("car_report2_json", "w") as f:
    json.dump(data, f, indent=4)
print("status: save to file successfully!:") 


