#با فایل 6-1 یکیه که همه درcar_report2_json هستن
import json
with open("car_report2_json", "r")as f:
    data = json.load(f)
min_capacity = data["min_capacity"]
battery = data["battery"]
engine_temp = data ["engine_temp"]
status = "moving"
while battery >= 5:
    print(f"current battery: {battery}%")
    if engine_temp >= engine_temp:
        print("stop now!")
        break
    if battery <= min_capacity:
        print("LOW BATTERY, please find charging station")
        print("low battery 10% every 100 km")
        battery = battery - 10
    if battery == 0:
       battery = 0
       print("STOP CAR! NO CHARG")
    
   

data["battery"] = battery
data ["engine_temp"] = engine_temp 
with open("car_report2_json", "w")as f:
     json.dump(data, f, indent=4)
print("status: data saved to file successfully!")                