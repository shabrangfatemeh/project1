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
            "LIMIT_TEMP": 200        #این به جای CRITICAL اومد
            },
            "battery": {
            "BATTERY_DROP": 5,
            "min_capacity": 15
            }
           }
# variable
MAX_TEMP = data ["engine_temp"]["MAX_TEMP"]
TEMP_RISE = data ["engine_temp"]["TEMP_RISE"]
current_temp = data["engine_temp"]["TEMP_RISE"]   #اینم اضافه کردیم تا بتوانم منطق IFدرست شود
BATTERY_DROP = data ["battery"]["BATTERY_DROP"]
min_capacity = data ["battery"]["min_capacity"]
passenger_car = input("what's your name?:")    
print(f"hi, welcome, {passenger_car}:")
#به دلیل نبود سنسور از مین و رایس استفاده کردم که در روز 11 اصلاح می شود
print(f"status current battery: {min_capacity} ")
print(f"status current engine_temp: {current_temp}")
#start while
while min_capacity > 0:
    choes1 = input("do you whant to stops along the way?: (y/n): ")
    if choes1 == "y":
        choes2 = input("where do you want to stope?:")
        print(f"target locked: {choes2}. moving now...")
        for i in range(3):
            min_capacity = min_capacity - BATTERY_DROP
            current_temp = current_temp + TEMP_RISE
            print(F"on the way to {choes2}... battery: {min_capacity}% | temp: {current_temp}")
            time.sleep(1)
            print(f"car reached{choes2}.")
            break
    if choes1 == "n":
        print("continue the way")
    time.sleep(1)
    min_capacity = min_capacity - BATTERY_DROP
    print(f"the each stage {BATTERY_DROP}: ")
    time.sleep(1)
     #برای دما حرفه ی تر عمل می کنیم
    current_temp = current_temp + TEMP_RISE
    if current_temp > 200:
        print("EMERGENCY! URGENT STOP!")
        break
       

data ["engine_temp"]["MAX_TEMP"] = current_temp
data ["engine_temp"]["TEMP_RISE"] = TEMP_RISE
data ["battery"]["BATTERY_DROP"] = BATTERY_DROP
data ["battery"]["min_capacity"] = min_capacity

with open("car_report2_json", "w") as f:
    json.dump(data, f, indent=4)
print("status: save to file successfully!:")
