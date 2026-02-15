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











 

#information from the user get
               
    print(f"moving: {address}")

   

    
            if stop_distance < 0:
                stop_distance = abs(stop_distance)
        except ValueError:
            stop_distance = 5
            print("invalid value, stop set at 5 km")                
      
    
   
    current_battery = car_info['current_battery']
    current_engine_temp = car_info['current_engine_temp']
    current_air_temp = car_info['current_air_temp']
    oil_level = car_info['oil_level']
    water_level = car_info['water_level']
    system_health = car_info['system_health']

    

        #LOOP
    while distance_traveled < CarConstants.TOTAL_DISTANCE:
        # UPDATE BATTERY AND TEMP

        current_battery, current_engine_temp = smart_sensor_battery_temp(current_battery, current_engine_temp,
            distance_traveled, current_air_temp, car_info['battery_drop'], car_info['temp_rise'])        

        distance_traveled = +1
        #calculate SYSTEM_HEALTH
        system_health = calculate_system_health(current_battery, current_engine_temp, oil_level, water_level,
                                                    car_info['max_battery'], car_info['critical_temp']
                                                    )    
        #show status            
        print(f"\n km: {distance_traveled}")
        print(f"battery: {current_battery:.1f}%")
        print(f" engine_temp: {current_engine_temp:.1f}°c")
        print(f"air_temp: {current_air_temp:.1f}°c")
        print(f"system_health: {system_health}%")

        #warning temp high
        if current_engine_temp >= car_info['critical_temp']:
            print("WARNING! engine overheated")
            print("STOP EMERGENCY!")
            break
        # REVIEW stop distance
        if stop_distance and distance_traveled == stop_distance:
            print(f"\n stop: {stop_address}")
            print(" A RELAX SHORT")
            time.sleep(3)
            print("continue travel")
        #warning battery weak
        if current_battery < car_info['critical_battery']:
            print("warning! battery is ending")
        # add error to list
        if "errors" not in car_info['data']["diagnostics"]:
            car_info['data']["diagnostics"]["errors"] = []
        car_info ['data']["diagnostics"]["errors"].append({
            "time": time.time(),
            "type": "battery_depleted",
            "message": "battery long trip ending"
        })           
        break
        time.sleep(1.5)
   
   #review complete trip
    if distance_traveled >= CarConstants.TOTAL_DISTANCE:
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
         car_info['data']["status"]["current_mode"] = "idle"
    else:
        print("❌ UNFINALISHED trip! the reason unknwon")
        car_info['data']["status"]["current_mode"] = "error"  

# save hn file jeson
    try:
        car_info['data']["battery"]["curent_leval"] = int(current_battery)
        car_info['data']["engine_temp"]["current_temp"] = current_engine_temp
        car_info['data']["engine_temp"]["current_air_temp"] = current_air_temp
        car_info['data']["fluids"]["oil_level"] = oil_level
        car_info['data']["fluids"]["water_level"] = water_level
        car_info['data']["system_health"] = system_health
        car_info['data']["status"]["is_active"] = False
        
        file_path = os.path.join(os.path.dirname(__file__), "car_report2_json")
        with open("file_path", "w") as f:
            json.dump(car_info['data'], f,indent=4)
        print("\n save file in json sucessfully")
    except Exception as e:
        print(f"\n . error in save file")
    #RUN the program
if __name__ == "__main__":
    main()

