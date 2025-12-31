import json


driver_name = input("what is your name?:")
print("hi, wellcom driver_name")

battery_driver = input(int("how much percentage of charge was added?: "))
print("battery_driver", battery_driver)

def add(battery_driver):
    print(f"battery driver:", {battery_driver + 85})

    print("report")
    print("status: data savedto file succssfully!")
