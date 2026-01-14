def garden_operations():
    # ValueError
    num_flowers = int("ouassim")
    print(num_flowers)

    # zeroDivisionError
    print("Testing ZeroDivisionError...")
    plant_height = 25 / 0
    print(plant_height)

    # FileNotFoundError
    open("missing.txt")

    # KeyError
    my_dict = {"plant": "tree"}
    print(my_dict['missing'])


def test_error_types():
    print("=== Garden Error Types Demo ===")

    try:
        int("one")
    except ValueError as e:
        print("\nCaught ValueErrr:", e)

    try:
        print(12/0)
    except ZeroDivisionError as e:
        print("\nCaught ZeroDivisionError:", e)

    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print("\nCaught FileNotFoundError:", e)

    try:
        plant = {'age': 12}
        print(plant['missing'])
    except KeyError as e:
        print("\nCaught KeyError:", e)

    # Testing multiple errors together
    print("\nTesting multiple errors together...")
    try:
        garden_operations()
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
