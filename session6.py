import json


driver_name = input("what is your name?:")
print(f"hi, wellcom {driver_name}")

current_battery = int(input("how much percentage of charge was added?: "))
print("battery_driver", current_battery)

def add(battery_added_percent):
    increased = battery_added_percent + 85
    print(f"current_battery:", {increased})

    print("report")
    car_data = {"driver_name": name, "increased": battery_added_percent + 85}
    with open("car_report.json", "w") as f:
    json.dump(car_data, f, indent=4) 
    print("status: data savedto file successfully!")

add(current_battery) 