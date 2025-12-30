import random
import time
def engine_temp():
       temp = random.randint(50, 120)
       return temp
while True:
    i = engine_temp()
    print("random generated temp:", engine_temp)
    if i > 100:
        print("WARNING! down engine_temp")
        break
time.sleep(5)
print("after 5 sec ...\n")
    

