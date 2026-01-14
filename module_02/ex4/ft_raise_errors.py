def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         " is too high (max 10)")

    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         " is too low (min 1)")

    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         " is too low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         " is too high (min 12)")

    print(f"Plant {plant_name} is healthy")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        check_plant_health('tomatos', 5, 6)
    except ValueError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        check_plant_health('', 9, 4)
    except ValueError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health('tomatos', 14, 10)
    except ValueError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health('tomatos', 6, 25)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
