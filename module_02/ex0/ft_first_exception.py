def check_temperature(temp_str: str):
    try:
        temp_int = int(temp_str)
    except Exception:
        print(f"Error: {temp_str} is not a valid number!")
        return None
    if temp_int >= 0 and temp_int <= 40:
        print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int
    elif temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
    else:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
