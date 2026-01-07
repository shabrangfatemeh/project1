import time
import json
with open("car_report2_json" "r")as f:
        data = json.load(f)
   #error
try:
      #def sensor_battery
    def sensor_battery(current_battery, BATTERY_DROP):
        return current_battery - BATTERY_DROP
except PermissionError:
    print("limited access: initializing default data..")
    data = {"BATTERY_DROP": 8}
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
    print(f"name: {passenger}")
    #fixed
CRITICAL_TEMP = data["engine_temp"]["CRITICAL_TEMP"]
TEMP_RISE = data["engine_temp"]["TEMP_RISE"]
BATTERY_DROP = data["battery"]["BATTERY_DROP"]
    # variable
current_temp = 50
current_battery = data["battery"]["max_capacity"]
     #
     




while sensor_temp >= CRITICAL_TEMP:
     









     # erroe try

   