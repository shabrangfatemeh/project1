import json
with open("car_report.json" "r") as f:
    data = json.load(f)

min_threshold = data["min_threshold"]
battery = data["battery"] 
status = "car_moving"

while battery > 0:
    print(f"current battery: %{battery}")

    if battery <= min_threshold:
    print("LOW BATTERY! please find e charging ststion")
    print("status: driving after 100 km, the battery low %5.")

    battery = battery - 5

    if  battery == 0:
        battry = 0
        print("CAR STOPPED! need charges.")

data["battery"] = battery
with open("car_report.json""w")as f:
    json.dump(data, f, indent=4)
print("status: data saved to file successfully!")