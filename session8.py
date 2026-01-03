#با فایل 6-1 یکیه که همه درcar_report2_json هستن
import json
try:
    with open("car_report2_json", "r")as f:
        data = json.load(f)
except FileNotFoundError:
    print("no report found!enter bot_02 initializing default data ...")
    data = {
        "battery": {
        "min_capacity": 20,
        "battery": 60
        },
        "engine_temp": 150,
    }
       
passenger_name = input("waht is your name? ")
print(f"hi, wellcome. {passenger_name}")
min_capacity = data["battery"]
battery = data["battery"]["current_level"]
engine_temp = data ["engine_temp"]
status = "moving"
while battery >= 5:
    print(f"current battery: {battery}%")
    if engine_temp >= engine_temp:
        print("stop now!")
        break
    passenger_name = input("would you like to stope every 300 km?: (y) or (no)")
    if passenger_name == "y": 
        print("STOP!")
        break
    elif passenger_name != "no":
        print("enter the distance you want stop?: ")
    if battery <= min_capacity:
        print("LOW BATTERY, please find charging station")
        print("low battery 10% every 100 km")
        battery = battery - 10
    if battery == 0:
       battery = 0
       print("STOP CAR! NO CHARG")
    
   
data["passenger_name"] = passenger_name
data["battery"]["current_level"] = battery
data ["engine_temp"] = engine_temp 
with open("car_report2_json", "w")as f:
     json.dump(data, f, indent=4)
print("status: data saved to file successfully!")                