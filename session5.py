import json
with open("car_report.json", "r") as f:
    data = json.load(f)
    print(data["battery"])   #1 
    print("battery level from file is:", data["battery"])   #2
 #به دو روش print نوشته می شود 