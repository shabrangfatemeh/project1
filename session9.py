import time
import json
try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)

except FileNotFoundError:
     print("not find! initializing default data ...")
     data = {
         "battery": {
         "min_capacity": 15,
         "current_level": 85
         },
         "engine_temp": 150
        } 
passenger_name = input("what is your name?:")
print("hi, wellcome passenger_name")
time.sleep(1)
print("continue after 2 sec")
battery = data["battery"]["current_level"]
min_capacity = data["battery"]
engine_temp = data["engine_temp"]
while battery  >= 10:
    time.sleep(2)
    print("continue after 3 sec") 
    print("battery current_level")
    print("every 100 km, low battery 5%")
    if engine_temp > 150:
        print("DANGER! STOP!")
        break
    passenger_name = input("do you want to stopevery 100 km? (y) or (n)")
    if passenger_name == "y":
        print("stop!")
        break
    if battery >= 15:
        print("EMERGENCY! please find a charging station.")
data = battery["current_level"]
data = ["engine_temp"]
with open("car_report2_json" "w") as f:
    json.dump = (data, f, indent=4)
print("status: data save to file successfully!")
