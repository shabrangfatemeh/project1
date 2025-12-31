import json
car_data = {"car_id": "bot_01", "battery": 112, "engine_temp": 112, 
            "status": "moving", "location": {"lat": 35.6892, "lng":51.3890}
            }
report = json.dumps(car_data, indent=4)
print("---copy the json below and send it to me ---")
with open("car_report.json", "w") as f:
    json.dump(car_data, f, indent=4)
    print("status: data saved to file successfully!")