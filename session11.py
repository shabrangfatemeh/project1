import time
import json
def battery_sensor(current_val):
    new_val = current_val - 8
    return new_val
def temp_sensor(current_val):
    new_val = current_val + 15
    return new_val

STOP_TEMP = 120
LOW_BATTERY = 20
try:
    with open("car_report2_json", "r") as f:
        status = json.load(f)
except FileNotFoundError:
    status = {"current_battery": 100, "current_temp": 30}
battery = status["current_battery"]
temp = status["current_temp"]    
    # اجرای عملیات
print(f"--- activate senssor system ---")

passenger = input("what's your name?:")
print(f"hi, welcom, {passenger}:")
address_passenger = input("enter the address:")
print(f"moving: {address_passenger}:")
while True:
    # به روز رسانی مقادیر بر اساس توابع
    battery = battery_sensor(battery)
    temp = temp_sensor(temp)
    if temp >= STOP_TEMP:
        print("EMERGENCE! stope!")
        break
    if battery <= LOW_BATTERY: 
        print("PLEAS stope!")
        break 
    time.sleep(1)

    choes1 = input("Are you stopping along the way?(y/n): ")
    if choes1 == "y":
       print("where do you stop?: ")
      
status["current_battery"] = battery
status["current_temp"] = temp 
with open("car_report2_json", "w") as f:
    json.dump(status, f,indent=4)
print("save to file successfully")    
     