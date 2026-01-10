def ft_seed_inventory(type: str, quantity: int, unit: str):
    type = type.capitalize()
    if unit == "packets":
        print(f"{type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{type} seeds: covers {quantity} square meters")
