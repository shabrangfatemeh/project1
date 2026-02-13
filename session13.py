import time
import json
try:
    with open("car_report2_json", "r") as f:
        data = json.load(f)
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
            if new_temp < data["battery"]["CRITICAL_BATTERY"]:
                print("CAUTION! battery low (<20%)")
            return max((new_battery, 0), new_temp)
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
oil_level = data["fluids"]["oil_level"]
water_level = data["fluids"]["water_level"]                                                                          
REV = 100
BATTERY_DROP_RATE = 2
TEMP_INCREASE_RATE = 5
current_temp = data["engine_temp"]["current_temp_air"]
current_battery = data["battery"]["max_capacity"]
distance_traveled = 0

                                # traveled
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
while distance_traveled < 10:
    current_battery, current_temp = smart_sensor_battery_temp(current_battery, BATTERY_DROP_RATE, current_temp, TEMP_INCREASE_RATE,
          distance_traveled, data["engine_temp"]["current_temp_air"], REV)
    distance_traveled = +1
        # calculathon system_health  محاسبه سلامت سیستم
    system_health = smart_sensor_system_health(current_battery, current_temp, oil_level, water_level)
    data["system_health"] = system_health
    print(f"step {distance_traveled+1}: battery={current_battery:.1f}, temp={current_temp:.1f}, system_health={system_health}")
           #warning high temp
    if current_temp >= data["engine_temp"]["max_temp"]:
        print("DANGER! High engine_temp!")
        break        
              #bet stop_way 
    if stop_distance and distance_traveled == stop_distance:
        print("stop! stop_way")
        break
    if address == address:
        print("arrive, enjoy traveled hope")
        break 
              
    time.sleep(2)
data["battery"]["max_capacity"] = int(current_battery)
data["engine_temp"]["current_temp_air"] = current_temp
data["fluids"]["oil_level"] = oil_level
data["fluids"]["water_level"] = water_level
with open("car_report2_json" "w") as f:
     json.dump(data, f,indent=4)
print("status: save file successfully")  
         
          





