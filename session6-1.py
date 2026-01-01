#ماشینی کهزمان رسیدن و خرابی و روغن وآب داره
import json
car_data = {"car_id": "bot_02", 
            "status": {
             "current_mode": "idle" 
             "is_active": true, 
             "charging": false
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
             "oil_level": 75
             "water_level": 90   
            },
            "location": {
             "latitude": 35.6892
             "longitude": 51.3890
             "last_updated": "2026-01-01T15:30:00Z"   
            },
            "diagnostics":{
             "errors": []   
            },
            "faults": []
            }