def ft_count_harvest_recursive():
    def recursive_count(days: int):
        if days == 0:
            return
        print(f"Day {days}")
        recursive_count(days - 1)
    days = int(input("Days until harvest: "))
    recursive_count(days)
    print("Harvest time!")
