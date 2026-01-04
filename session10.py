import json
import time
try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)
    #danger not file
except FileNotFoundError:    
    print("not find! initializing default data...")
    data = {
            "engine_temp": {
            "MAX_TEMP": 200,
            "TEMP_RISE": 10,
            "CRITICAL_TEMP": 200
            },
            "battery": {
            "BATTERY_DROP": 5,
            "min_capacity": 15
            }
           }
# variable
MAX_TEMP = data ["engine_temp"]["MAX_TEMP"]
TEMP_RISE = data ["engine_temp"]["TEMP_RISE"]
BATTERY_DROP = data ["battery"]["BATTERY_DROP"]
min_capacity = data ["battery"]["min_capacity"]
passenger_car = input("what's your name?:")    
print(f"hi, welcome, {passenger_car}:")
print("status current battery: ")
print("status current engine_temp: ")
#start while
while min_capacity < 15:
    time.sleep(1)
    print(f"the each stage {BATTERY_DROP}: ")
    time.sleep(1)
    if MAX_TEMP > 210:
        print("EMERGENCY! URGENT STOP!")
        break
    choes1 = input("do you whant to stops along the way?: (y/n)")
    if choes1 == "y":
        choes2 = ("where do you want to stope?:")
        print("street 45 m")
        break
    if choes1 == "n":
        print("continue the way")    

data ["engine_temp"]["MAX_TEMP"] = MAX_TEMP
data ["engine_temp"]["TEMP_RISE"] = TEMP_RISE
data ["battery"]["BATTERY_DROP"] = BATTERY_DROP
data ["battery"]["min_capacity"] = min_capacity
with open("car_report2_json", "w") as f:
json.dump(data, f, indent=4)
print("status: save to file successfully!:")
