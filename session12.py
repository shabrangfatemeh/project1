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
         "MAX_TEMP": 10,
         "TEMP_RISE": 10,
         "CRITICAL_TEMP": 200   
         }
    } 
      #def sensor_battery
def sensor_battery(current_battery, BATTERY_DROP, erroe_factor):
    try:
        return current_battery - BATTERY_DROP + erroe_factor
    except TypeError:
        return current_battery
    
       # def battery_distance
def battery_distance(sensor_battery, distance_traveled):
    return sensor_battery - distance_traveled
    #def temp
def sensor_temp(current_temp, TEMP_RISE):
    return current_temp + TEMP_RISE
 # def special
def warning_temp_high(red):
     print("red")
   # name passenger
def passenger(name):
    print(f"hi, welcom: {passenger}:")
    #fixed
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
    current_temp = sensor_temp(current_temp, TEMP_RISE)
    current_battery = sensor_battery(current_battery, BATTERY_DROP)
    sensor_battery = battery_distance(sensor_battery, distance_traveled)

    distance_traveled += 1

    print(f"battery: {current_battery}")
    print(f"temp: {current_temp}")
    print(f"sensor_battery: {battery}")
    print(f"distance_traveled : {distance_traveled} (km)")

    if sensor_temp >= CRITICAL_TEMP:
        print("warning! stop!")
        break
    if sensor_battery <= min_capacity:
        print("empty battery! stop!")
        break
    if stop_distance is not None and distance_traveled >= stop_distance:
        print(f"stop car at : {stop_address}")
        break
time.sleep(1)

data["battery"]["max_capacity"] =  current_battery      
data["engine_temp"]["MAX_TEMP"] =  current_temp 
data["battery"]["min_capacity"] = min_capacity

with open("car_report2_json" "w") as f:
     json.dump(data, f, indent=4)
print("status: file to save successfully: ")     