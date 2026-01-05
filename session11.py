import time
import json
def calculate_battery(current):
    return current - 7
def calculate_temp(current):
    return current + 12

MIN_BATTERY_LEVEL = 10
MAX_ENGINE_TEMP = 110 
try:
    with open("car_report2_json", "r") as f:
        status = json.load(f)
except FileNotFoundError:
    status = {"battery_percent": 100, "engine_temp": 25}
current_battery = status["battery_percent"]
current_temp = status["temp_percent"]    
    # اجرای عملیات
print(f"--- start 11 day ---")
print(f"fixt rules:temp allowed < {MAX_ENGINE_TEMP} | fixed rules:battery allowed > {MIN_BATTERY_LEVEL}")

passenger = input("what's your name?:")
print(f"hi, welcom, {passenger}:")
address_passenger = input("enter the address:")
print(f"moving: {address_passenger}:")
while true:
    # به روز رسانی مقادیر بر اساس توابع
    current_battery = calculate_battery(current_battery)
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
     