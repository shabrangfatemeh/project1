import json
car_data = {"car_id": "bot_01", "battery": 112,"engine_temp": 112,
            "status": "moving", "location": {"lat": 35.6892, "lang":51.3890}}
report = json.dumps(car_datd, indent=4)
print("---copy the json below and send it to me ---")
print(report)