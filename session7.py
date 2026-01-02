import json
with open("car_report.json", "r") as f:
    data = json.load(f)

min_threshold = data["min_threshold"]
battery = data["battery"] 
engine_temp = data["engine_temp"]
status = "car_moving"

while battery > 0:
    print(f"current battery: %{battery}")
    if engine_temp >= 115:
        print("STOP!")
        break
    if battery == 50:
       print("battry is helf or less: ")
    order_driver = input("continue(y) or stop(s)?")
    print("y" or "s")   
    if order_driver  == "s":
       print("STOPE!")
       break

    if battery <= min_threshold:
        print("LOW BATTERY! please find a charging ststion")
        print("status: driving after 100 km, the battery low %5.")

    battery = battery - 5

    if  battery == 0:
        battery = 0
        print("CAR STOPPED! need charges.")

data["battery"] = battery
data["engine_temp"] = engine_temp
with open("car_report.json", "w")as f:
    json.dump(data, f, indent=4)
print("status: data saved to file successfully!")
                                                                                                   