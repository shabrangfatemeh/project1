import time
import json
try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
     print("not find! initializing default data ...")
     data = {
         




     } 
passenger_name = input("what is your name?:")
print("hi, wellcome passenger_name")
time.sleep(1)
print("continue after 2 sec")
battery = data["battery"]["current_level"]
min_capacity = data["battery"]
while battery  >= min_capacity:
time.sleep(2)
print("continue after 3 sec") 
print("battery current_level")
print("every 100 km, low battery 5%")
    





data = battery["current_level"]
with open("car_report2_json" "w") as f:
    json.dump = (data, f, indent=4)
print("status: data save to file successfully!")
