while True:
    try:
        i = battery_level = 15
        b =engine_temp = 105
        if i < 20:
            print("Warning: Low Battery! Finding charger")
        elif b > 100:
            print("Warning: Over heating! Cooling down")
        else:
            print("All systems ok. You can drive")
        if i < 15 and b > 105:
            print("EMERGENCY stop!")