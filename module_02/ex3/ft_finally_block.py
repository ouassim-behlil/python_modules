def water_plants(plant_list: list[str]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("watering " + plant)
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    my_plants = ["tomato", "carrots", "lettuce"]
    water_plants(my_plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    my_plants = ['Tomato', None, 'carrots']
    water_plants(my_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
