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
        status = data.get("status", {})
        current_mode = status.get("current_mode", "idle")
        is_active = status.get("is_active", True)
        charging = status.get("charging", False)
# BATTERY         
        battery = data.get("battery", {})
        current_battery = battery.get("current_level", 85)
        min_battery = battery.get("min_capacity", 15)
        max_battery = battery.get("max_capacity",250)
        battery_drop = battery.get("BATTERY_DROP", 5)
        critical_battery = battery.get("CRITICAL_BATTERY", 20)
#ENGINE TEMP
        engine_temp = data.get("engine_temp", {})
        current_engine_temp = engine_temp.get("current_level", 25)        
        current_air_temp = engine_temp.get("current_air_temp", 25)
        temp_rise = engine_temp.get("TEMP_RISE", 10)
        critical_temp = engine_temp.get("CRITICAL_TEMP", 200)
#FLUIDS
        fluids = data.get("fluids", {})
        oil_level = fluids.get("oil_level", 75)
        water_level = fluids.get("water_level", 90)
# location
        location = data.get("location", {})
        latitude = location.get("latitude", 35.6892)
        longitude = location.get("longitude", 51.389)
# system_health
        system_health = data.get("system_health", 100)
#erorr                                
        diagnostics = data.get("diagnostics", {})
        errors = data.get("errors", {})
        faults = data.get("faults", {})

        return{
            "car_id": car_id,
            "current_mode": current_mode,
            "is_active": is_active,
            "charging": charging,
            "current_battery": current_battery,
            "min_battery": min_battery,
            "max_battery": max_battery,
            "battery_drop": battery_drop,
            "critical_battery": critical_battery,
            "current_enginy_temp": current_engine_temp,
            "current_air_temp": current_air_temp,
            "temp_rise": temp_rise,
            "critical_temp": critical_temp,
            "oil_level": oil_level,
            "water_level": water_level,
            "latitude": latitude,
            "longitude": longitude,
            "system_health": system_health,
            "errors": errors,
            "faults": faults,
            "data": data
        }

    except FileNotFoundError:
        print("Not file! initializing default data...")
        return None
    except json.JSONDecodeError:
        print(f"not file json: {e}")
        return None
    except Exception as e:
        print(f"Unknown error: {e}")
        return None
#function
def smart_sensor_battery_temp(current_battery, current_engine_temp, distance_traveled, current_air_temp, battery_drop, temp_rise):

    """ calculate status battery and temp"""
    try:
#calculate factors influential
         
        distance_factor = 1 + distance_traveled * 0.005
        new_engine_temp = (current_engine_temp + temp_rise + current_air_temp * 0.01)
        new_battery = current_battery - (battery_drop * distance_factor)
        return max(new_battery, 0), new_temp
    except Exception as e:
        print(f"sensor error: {e}")
        return current_battery, current_engine_temp

def calculate_system_health(current_battery, current_engine_temp, oil_level, water_level, max_battery, critical_temp):    
    """calculate all system health"""
    temp_factor = max(0, 1 - current_engine_temp / critical_temp) 
    battery_factor = current_battery / max_battery 
    fluids_factor =  (oil_level + water_level) / 200      #200 = max_oil + max_water
    system_health = (battery_factor + temp_factor + fluids_factor) / 3 * 100
    return min(max(int(system_health),0), 100)
  #   MAIN PROGRAM
def main():
    print("\n" + "="*50)
    print("simulator traveled to car")
    print("="*50)
                   
#load data json
    car_info = load_car_data()
    if not car_info:
        print("program json stop! file chek")
        return
    
#information car show
    print(f"id: {car_info['car_id']}")
    print(f"status:{car_info['current_mode']}")
    print(f"charge:{'yes' if car_info['charging'] else'no'}")
    print(f"status:{car_info['latitude']},{car_info['longitude']}")
    print("-"*50)

#information from the user get
    address = input("where is your destination?")            
    print(f"moving: {address}")

    stop_way = input("do you have any stope during your trip? : (y/n)").strip().lower()

    stop_distance = None
    stop_address = None

    if stop_way in ("yes","y"):
        stop_address = input("where do you want to stop?:")
        stop_distance = int(input("how many (km) do you have to stop?: "))

      #start trip
    print("\n"+"="*50)
    print("start trip")
    print("="*50)
    distance_traveled = 0
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

    if distance_traveled >= CarConstants.TOTAL_DISTANCE:
        print("✔️ you have reacherd your destination")
        car_info['data']["status"]["current_mode"] = "idle"
    elif current_battery <= 0:
        print("❌ UNFINALISHED trip! finish battery")
        car_info['data']["status"]["current_mode"] = "error"
    elif current_engine_temp >= car_info['critical_temp']:
        print("❌ UNFINALISHED trip! over the limit engine temp")
        car_info['data']["status"]["current_mode"] = "error"
    else:
        print("❌ UNFINALISHED trip! the reason unknwon")  

# save hn file jeson
    car_info['data']["battery"]["curent_leval"] = int(current_battery)
    car_info['data']["engine_temp"]["current_temp"] = current_engine_temp
    car_info['data']["engine_temp"]["current_air_temp"] = current_air_temp
    car_info['data']["fluids"]["oil_level"] = oil_level
    car_info['data']["fluids"]["water_level"] = water_level
    car_info['data']["system_health"] = system_health
    car_info['data']["status"]["is_active"] = False

    try:
        with open("car_report2_json", "w") as f:
            json.dump(data, f,indent=4)
        print("\n save file in json sucessfully")
    except Exception as e:
        print(f"\n . error in save file")
    #RUN the program
if __name__ == "__main__":
    main()

