import time
import json
def battery_sensor(current_battery, BATTERY_DROP):
    return current_battery - BATTERY_DROP
def temp_sensor(current_temp, temp_drop):
       return current_temp + temp_drop

try:
    with open("car_report2_json", "r") as f:
        status = json.load(f)
except FileNotFoundError:
   print("not find! initializing default data ...")
   data = {
       "engine_temp": {
       "MAX_TEMP": 200,
       "TEMP_RISE": 10,   
       },
       "battery": {
       "BATTERY_DROP": 5, 
       "MIN_CAPACITY": 20,
       "max_capacity": 250
       }
      }
   # fixed
MAX_TEMP = data ["engine_temp"]["MAX_TEMP"]
TEMP_RISE = data ["engine_temp"]["TEMP_RISE"]
BATTERY_DROP = data ["battery"]["BATTERY_DROP"]
   #
current_temp = 90
current_battery = data ["battery"]["max_capacity"]

passenger = input("what's your name?:")
print(f"hi, welcom, {passenger}:")
      #address
address = input("enter the address:")
print(f"moving: {address}:")
stop_Q = input("Are you stopping along the way?(y/n): ").strip().lower()
stop_address = None
stope_distance = None
if stop_Q in ("y", "yes"):
        stop_adderss = input("where do you stop?:")
        stop_distance = int (input("distance to stop(km): "))
traveled_distance = 0
     #while        
while True:
    current_temp = temp_sensor(current_temp, TEMP_RISE)
    current_battery = battery_sensor(current_battery, BATTERY_DROP)
    traveled_distance += 1
    print(f"battery: {current_battery}")
    print(f"temp: {current_temp}")
    print(f"traveled_distance: {traveled_distance} km")
     #if
    if current_temp >= 200
        print("danger! stop!")
        break 
    if current_battery <= 30:
        print("battery empty")
        break
    

    battery = battery_sensor(battery)
    temp = temp_sensor(temp)
    if temp >= STOP_TEMP:
        print("EMERGENCE! stope!")
        break
    if battery <= LOW_BATTERY: 
        print("PLEAS stope!")
        break 
    time.sleep(1)

   
status["current_battery"] = battery
status["current_temp"] = temp 
with open("car_report2_json", "w") as f:
    json.dump(status, f,indent=4)
print("save to file successfully")    
     