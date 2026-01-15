class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
