import json
whit open("car_report_json" "r") as f:
data = json.load(f)
battery = ["min_thershold"]

status = "car_moving"
battery = 25
while battery > 0:
    print(f"current battery: %{battery}")
    if battery <=10
    print("LOW BATTERY! please find e charging ststion")
    print("status: driving after 100 km, the battery low %5.")
    battery = battery - 5
    if  battery == 0:
        print("CAR STOPPED! need charges.")


whit open("car_report_json""w")as f:
json.dump(data, f, indent=4)
print("status: data saved to file successfully!")