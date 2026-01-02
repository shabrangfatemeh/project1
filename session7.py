status = "car_moving"
i = battery = 25
while battery > 0:
    print("status: driving after 100 km, the battery low %5.")
    battery = battery - 5
    if i == 0:
        print("CAR STOPPED! need charges.")