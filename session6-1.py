#ماشینی کهزمان رسیدن و خرابی و روغن وآب داره
import json
from datetime import datetime
i = datetime.now()
time_string = i.strftime("%H:%M:%S")

car_data = {"car_id": "bot_02", 
            "status": {
             "current_mode": "idle", 
             "is_active": True, 
             "charging": False
            }, 
            "battery": { 
             "min_capacity": 15,
             "max_copacity": 250,
             "current_level": 85,
             "unit": "percentage"
            },
            "max_spead": 350,
            "engine_temp": 150,
            "fluids": {
             "oil_level": 75,
             "water_level": 90   
            },
            "location": {
             "latitude": 35.6892,
             "longitude": 51.3890,
             "last_updated": "time_string"   
            },
            "diagnostics":{
             "errors": []   
            },
            "faults": []
            }
report = json.dumps(car_data, indent=4)
print("--- copy the json below and send it to me ---")
with open ("car_report2_json", "w") as f:
    json.dump (car_data, f, indent=4)
    print("--- status: data saved to file successfully! ---")
last_time_str = car_data["location"]["last_updated"]
translated_time = datetime.strptime(last_time_str, "%Y-%M-%DT%H:%M:%SZ")
diff = datetime.now() - translated_time
print(f"{diff}:")