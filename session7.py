import json
with open("car_report.json" "r") as f:
data = json.load(f)
min_threshold = data["min_threshold"]

status = "car_moving"
battery = data["battery"] 
while battery > 0:
    print(f"current battery: %{battery}")
    if battery <= 10:
    print("LOW BATTERY! please find e charging ststion")
    print("status: driving after 100 km, the battery low %5.")
    battery = battery - 5

    if  battery == 0:
        print("CAR STOPPED! need charges.")


with open("car_report.json""w")as f:
json.dump(data, f, indent=4)
print("status: data saved to file successfully!")