import random
import time
def status():
    engine_temp = random.randint(50, 120)
    buttry_level = random.randint(0, 100)
    return buttry_level, engine_temp   
while True:
    buttry_level, engine_temp = status()
    print("random generated engine_temp:", engine_temp)
    print("random generated buttry_level:", buttry_level)
    if buttry_level < 15 and engine_temp > 105:
        print("EMERGENCY stop!")
        break
    if engine_temp > 100:
        print("WARNING! down engine_temp")
    if buttry_level < 20:
        print("WARNING:Low Buttery! Finding charger")
       
time.sleep(5)
print("after 5 sec ...\n")
    

