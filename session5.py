import json
with open("car_report.json", "r") as f:
    data = json.load(f)
    print(data["battry"])