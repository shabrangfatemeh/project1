import json


driver_name = input("what is your name?:")
print(f"hi, wellcom {driver_name}")

charge_to_add = int(input("how much charge are you adding?: "))
print("battery_driver", charge_to_add)

def update_car_system(added_amount):
    with open("car_report.json", "r") as f:
         data = json.load(f)
    current_status = data["min_threshold"]
    new_total =  current_status + added_amount 
    data["battery"] = new_total
    data["driver"] = driver_name
    data["min_threshold"] = 10
    with open("car_report.json", "w") as f:
        json.dump(data, f, indent=4) 
    print(f"update successfully! battery went from {current_status}% to {new_total}%")
    if new_total <= 10:
        print("WARNING!: battery is at or below minium level!")

update_car_system(charge_to_add) 