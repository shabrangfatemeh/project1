import time
import json
 
 
print("\n" + "="*50)
print("simulator traveled to car")
print("="*50)

try:
    with open("car_report2_json" "r")as f:
        data = json.load(f)
except FileNotFoundError:
        print("not found! initializing default data...")
        exit()
except json.JSONDecodeError:
        print("❌invalid json format")
        exit()    
# CONFIG JSON
current_battery = data["battery"]["current_level"]
current_temp = data["engine_temp"]["current_engine_temp"]
current_air_temp = data["engine_temp"]["current_air_temp"]
oil_level = data["fluids"]["oil_level"]  
water_level = data["fluids"]["water_level"]
max_battery = data["battery"]["max_capacity"]
critical_battery = data["battery"]["CRITICAL_BATTERY"]
critical_temp = data["engine_temp"]["CRITICAL_TEMP"]
battery_drop_rate = 2
temp_rise_rate = 5
rev = 100

print(f"initial battery: {current_battery}%")
print(f"initial temp: {current_temp}°c")
print(f"critical battery: {critical_battery}%")
print(f"critical temp: {critical_temp}°c")    
# input USER        
address = input("where is your destination?") 
stop_way = input("do you have any stope during your trip? : (y/n)").strip().lower()

stop_distance = None
stop_address = None

if stop_way in ("yes","y"):
    
    
    stop_address = input("where do you want to stop?:")
    stop_distance = int(input("how many (km) do you have to stop?: "))  

#function
def smart_sensor_battery_temp(current_battery, current_temp, distance, current_air_temp, rev):

   
#calculate factors influential
         
    distance_factor = 1 + distance * 0.005
   
    new_temp = current_temp + temp_rise_rate + (current_air_temp * 0.01) + (rev * 0.01)
    new_battery = current_battery - (battery_drop_rate * distance_factor * rev)

    if new_battery < 0:
        new_battery = 0

    return new_battery, new_temp


def system_health(current_battery, current_engine_temp, oil_level, water_level, max_battery, critical_temp):    
#calculate all system health
    temp_factor = max(0, 1 - (current_engine_temp / critical_temp)) 
    battery_factor = current_battery / max_battery 
    fluids_factor =  (oil_level + water_level) / 200      #200 = max_oil + max_water
    system_health = (battery_factor + temp_factor + fluids_factor) / 3 * 100
    return min(max(0, min(100,system_health)))
#start trip
print("\n"+"="*50)
print("start trip")
print("="*50)               
distance_traveled = 0
trip_completed = False
stop_reason = ""
   #LOOP
while distance_traveled < 10:
    # UPDATE BATTERY AND TEMP

    current_battery, current_engine_temp = smart_sensor_battery_temp(current_battery, current_temp,
        distance_traveled, current_air_temp, rev)        

    distance_traveled = +1
#calculate SYSTEM_HEALTH
    system_health = system_health(current_battery, current_engine_temp, oil_level, water_level)
#show status            
    print(f"\n km: {distance_traveled}")
    print(f"battery: {current_battery:.1f}%")
    print(f" engine_temp: {current_engine_temp:.1f}°c")
    print(f"air_temp: {current_air_temp:.1f}°c")
    print(f"system_health: {system_health}%")
#warning battery weak
    if current_battery < critical_battery:
        print("warning! battery is ending")                                                   
#warning temp high
    if current_temp >= critical_temp:
        print("WARNING! engine overheated")
        stop_reason = "engine overheated"
        break                                                
 # REVIEW stop distance
    if stop_distance and distance_traveled == stop_distance:
        print(f"\n stop: {stop_address}")
        time.sleep(2)
        print(" A RELAX SHORT")
        time.sleep(1)
        print("continue travel")
#review complete trip
    if distance_traveled == 10:
        trip_completed = True
        stop_reason = "arrive to destination"
#SUMMARY TRIP 
    print("\n" + "="*50)
    print("summary trip")
    print("="*50)
    print(f"destination :{address}")
    if stop_address:
        print(f"stop:{stop_address}")
    print(f"distance traveled:{distance_traveled} km")
    print(f"final battery:{current_battery:.1f}%")
    print(f"final engine temp:{current_engine_temp:.1f}°c")
    print(f"final system health:{system_health}%")

    if trip_completed:
        print("✔️ you have reacherd your destination")
        data["status"]["current_mode"] = "error"

    else:
        print("❌ UNFINALISHED trip! the reason unknwon")
        data = ["status"]["current_mode"] = "error"  
# save in file jeson
        data["battery"]["curent_leval"] = int(current_battery)
        data["engine_temp"]["current_engine_temp"] = current_temp
        data["engine_temp"]["current_air_temp"] = current_air_temp
        data["fluids"]["oil_level"] = oil_level
        data["fluids"]["water_level"] = water_level
        data["system_health"] = system_health
        data["status"]["is_active"] = False   
    try:                                             
                  
        with open("file_path", "w") as f:
            json.dump(data, f,indent=4)
        print("\n save file in json sucessfully")
    except Exception as e:
        print("\n error in save file")
    print("="*50)

