def ft_water_reminder():
    watering_days = int(input("Days since last watering: "))
    if watering_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
