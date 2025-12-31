import random
import time
def status(engine_temp, buttry_level):
    engine_temp = random.randint(50, 120)
    return engine_temp
    buttry_level = random.randint(0, 100)
    return buttry_level   
while True:
    i = engine_temp =15
    b = buttry_level =105
    print("random generated engine_temp:", engine_temp)
    print("random generated buttry_level:", buttry_level)
    if b < 15 and i > 105:
        print("EMERGENCY stop!")
    if i > 100:
        print("WARNING! down engine_temp")
    for buttry_level in (0, 100):
        if b < 20:
        print("WARNING:Low Buttery! Finding charger")
        break
time.sleep(5)
print("after 5 sec ...\n")
    

