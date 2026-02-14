import time
import json
      #fix constants
class CarConstants:
    BATTRY_DROP_RATE = 5
    CRITICAL_BATTERY = 20
    CRITICAL_TEMP = 200
    TEMP_RISE_RATY = 10
    MAX_SPEED = 350
    TOTAL_DISTANCE = 10

def load_car_data():
    try:
        with open("car_report2_json", "r") as f:
            data = json.load(f)
# CONFIG JSON
        car_id = data.get("car_id", "bot_02")
#status
        status = data.get("status",{})
        current_mode = status.get("current_mode", "idle")
        is_active = status.get("is_active", True)
        charging = status.get("charging", False)
# BATTERY         
        battery = data.get("battery",{})
        current_battery = battery.get("current_level", 85)
        min_battery = battery.get("min_capacity", 15)
        max_battery = battery.get("max_capacity",250)
        battery_drop = battery.get("BATTERY_DROP", 5)
        critical_battery = battery.get("CRITICAL_BATTERY", 20)
#ENGINE TEMP
                

    current_temp = data["engine_temp"]["current_temp_air"]
    current_battery = data["battery"]["current_capacity"]
    oil_level = data["fluids"]["oil_level"]
    water_level = data["fluids"]["water_level"] 

except PermissionError:
    print("file promission! initializing default data...")
    
    data = {
        "battery": {
        "min_capacity": 10,
        "max_capacity": 200,
        "CRITICAL_BATTERY": 20
        },
        "engine_temp": {
        "MAX_TEMP": 150,
        "TEMP_RISE":5,
        "current_temp_air": 25
        },
        "fluids": {
        "oil_level": 100,
        "water_level": 100     
        },
        "system_health": 100
       } 
           #  def    smart   sensor    battery   ,   temp

def smart_sensor_battery_temp(current_battery, BATTERY_DROP_RATE, current_temp, TEMP_INCREASE_RATE, distance_traveled, current_temp_air, REV):
    try:
            distance_factor = 1 + distance_traveled * 0.005
            REV_factor = 1 + REV * 0.003
            new_temp = current_temp + TEMP_INCREASE_RATE + current_temp_air * 0.01 + REV * 0.01
            new_battery = current_battery - BATTERY_DROP_RATE * distance_factor  * REV_factor
              #BET  BATTERY
            if new_battery < data["battery"]["CRITICAL_BATTERY"]:
                print("CAUTION! battery low (<20%)")
            return max(new_battery, 0), new_temp
    except TypeError:
            return current_battery, current_temp
                               #def health
def smart_sensor_system_health(current_battery, current_temp, oil_level, water_level):
    
    temp_factor = max(0, 1 - current_temp / data["engine_temp"]["max_temp"]) 
    battery_factor = current_battery / data["battery"]["max_capacity"] 
    fluids_factor =  oil_level + water_level / 200 # فرض حداکثر مجموع
    system_health = (battery_factor + temp_factor + fluids_factor) / 3 * 100
    return min(max(int(system_health),0), 100)
                                # config
                                            #FIXd or  # variable
                                                                        
REV = 100
BATTERY_DROP_RATE = 2
TEMP_INCREASE_RATE = 5

distance_traveled = 0

                                # traveled
print("===car trip simulator===")                                
address = input("where you want the way? : ")
print(f"moving: {address}:")
stop_way = input("do you want stop along the way?: (y/n): ").strip().lower()
                #       no addresss no distance
stop_address = None
stop_distance = None
                
if stop_way in ("yes", "y"):
        stop_address = input("where do you want to stop?: ")
        stop_distance = int(input("distance you stop?: (km): "))

           #LOOP
print("\n===starting trip===")
total_distance = 10           
while distance_traveled < total_distance:

    current_battery, current_temp = smart_sensor_battery_temp(current_battery, BATTERY_DROP_RATE, current_temp, TEMP_INCREASE_RATE,
          distance_traveled, data["engine_temp"]["current_temp_air"], REV)
    distance_traveled = +1
        # calculathon system_health  محاسبه سلامت سیستم
    system_health = smart_sensor_system_health(current_battery, current_temp, oil_level, water_level)
    data["system_health"] = system_health
         #نمایش وضعیت
    print(f"\nstep {distance_traveled}:")
    print(f"battery:{current_battery:.1f}%")       
    print(f"temp:{current_temp:.1f}°c")
    print(f"system_health:{system_health}%")
              #bet stop_way 
    if distance_traveled >= total_distance:
        print("stop! successfully reached destination")
    elif current_battery <= 0:
        print("✖️ trip interrupted: battery depleted")     
           #warning high temp
    elif current_temp >= data["engine_temp"]["max_temp"]:
        print("✖️ trip interrupted: engine overheated")
    else:
        print("✖️trip interrupted: unknown reason")
        #save data        
    time.sleep(2)
data["battery"]["max_capacity"] = int(current_battery)
data["engine_temp"]["current_temp_air"] = current_temp
data["fluids"]["oil_level"] = oil_level
data["fluids"]["water_level"] = water_level
with open("car_report2_json" "w") as f:
     json.dump(data, f,indent=4)
print("status: save file successfully")  
         
          





