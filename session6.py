import json


driver_name = input("what is your name?:")
print(f"hi, wellcom {driver_name}")

current_battery = int(input("how much percentage of charge was added?: "))
print("battery_driver", current_battery)

def add(battery_added_percent):
    increased = battery_added_percent + 85
    print(f"current_battery:", {increased})

    print("report")
    with open("car_report.json", "r") as f:
        data = json.load(f)
    data["driver"] = driver_name
    data["base_battery"] = 85
    data["added_battery"] = increased
    with open("car_report.json", "w") as f:
        json.dump(data, f, indent=4) 
        print("status: data saved to file successfully!")

add(current_battery) 