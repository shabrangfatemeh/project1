 MAX_BATTERY = 200
    MIN_BATTERY = 10
    CRITICAL_BATTERY = 20
    MAX_TEMP = 150
    MAX_OIL = 100
    MAX_WATER = 100



#fix constants
class CarConstants:
    BATTRY_DROP_RATE = 5
    CRITICAL_BATTERY = 20
    CRITICAL_TEMP = 200
    TEMP_RISE_RATY = 10
    MAX_SPEED = 350
    TOTAL_DISTANCE = 10


if distance_traveled >= CarConstants.TOTAL_DISTANCE:
   
   car_info['data']["status"]["current_mode"] = "idle"
    elif current_battery <= 0:
        print("❌ UNFINALISHED trip! finish battery")
        car_info['data']["status"]["current_mode"] = "error"
    elif current_engine_temp >= car_info['critical_temp']:
        print("❌ UNFINALISHED trip! over the limit engine temp")
        car_info['data']["status"]["current_mode"] = "error"