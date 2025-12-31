import json


driver_name = input("what is your name?:")
print(f"hi, wellcom {driver_name}")

battery_driver = int(input("how much percentage of charge was added?: "))
print("battery_driver", battery_driver)

def add(battery_added_percent):
    increased = battery_added_percent + 85
    print(f"battery driver:", {increased})

    print("report")
    print("status: data savedto file successfully!")

add(battery_driver) 