#با فایل 6-1 یکیه که همه درcar_report2_json هستن
import json
with open("car_report2_json", "r")as f:
    data = json.load(f)
min_capacity = data["min_capacity"]
battery = data["battery"]
status = "moving"
while battery <= 5:
    print()