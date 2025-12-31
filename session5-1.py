import json
with open("car_report.json", "r") as f:
    recovered_data = json.load(f)
print("--- data_recovered successfully ---")
print(f"car ID: {recovered_data['car_id']}")
print(f"current battery: {recovered_data['battery']}%")
if recovered_data['battery'] < 20:
    print("action required: low battery detected in history!")    