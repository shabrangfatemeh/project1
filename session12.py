import time
import json
try:
    with open("car_report2_json" "r")as f:
        data = json.load(f)
except FileNotFoundError:
    print("not found! initializing default data...")
    data = {
         "battery": {
         "min_capacity": 15,
         "max_capacity": 250,     
         "BATTERY_DROP": 8
         },
         "engine_temp": {
         "MAX_TEMP": 100,
         "TEMP_RISE": 10,
         "CRITICAL_TEMP": 200   
         }
    } 
      #def sensor_battery
def smart_battery(current_battery, distance_traveled, current_temp, BATTERY_DROP):
    try:
        temp_factor = 1 + (current_temp - 25) * 0.01
        distance_factor = 1 + distance_traveled * 0.005
        new_battery = current_battery - BATTERY_DROP * temp_factor * distance_factor 
        return int(max(new_battery, 0))
    except TypeError:
        return current_battery
       #def temp
def sensor_temp(current_temp, TEMP_RISE, error_factor):
    try:
        return current_temp + TEMP_RISE - error_factor
    except TypeError:
        return current_temp
  # def special
def warning_temp_high():
     print("red warning!temp_high")
   # name passenger
def passenger(name):
    print(f"hi, welcome: {name}:")
    # config fixed
CRITICAL_TEMP = data["engine_temp"]["CRITICAL_TEMP"]
TEMP_RISE = data["engine_temp"]["TEMP_RISE"]
BATTERY_DROP = data["battery"]["BATTERY_DROP"]
    # variable
current_temp = 50
current_battery = data["battery"]["max_capacity"]
min_capacity = data["battery"]["min_capacity"]
     #traveled
address = input("where is your distination?:")
print(f"moving: {address}: ")
car_stop = input("do you whant stop along the way?: (y/n): ").strip().lower()
      # no address and distance
stop_address = None
stop_distance = None
      # if
if car_stop in ("y", "yes"):
        stop_address = input("where do you want to stop?: ")
        stop_distance = int(input("distance you stop(km): "))
distance_traveled = 0
        #loop
while True:
    current_temp = sensor_temp(current_temp, TEMP_RISE, 0)
    current_battery = smart_battery(current_battery, distance_traveled, current_temp, BATTERY_DROP)
    
    distance_traveled += 1

    print(f"smart_battery: {current_battery}")
    print(f"temp: {current_temp}")
    print(f"distance_traveled : {distance_traveled} (km)")

    if current_temp >= CRITICAL_TEMP:
        print("warning! stop!")
        break
    if current_battery <= min_capacity:
        print("empty battery! stop!")
        break
    if stop_distance is not None and distance_traveled >= stop_distance:
        print(f"stop car at : {stop_address}")
        break
time.sleep(1)

data["battery"]["max_capacity"] = int(current_battery)      
data["engine_temp"]["CRITICAL_TEMP"] = current_temp 

with open("car_report2_json" "w") as f:
     json.dump(data, f, indent=4)
print("status: file to save successfully: ")     