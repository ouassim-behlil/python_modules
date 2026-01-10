def ft_harvest_total():
    total = 0
    i = 1
    while i < 4:
        total += int(input(f"Day {i} harvest: "))
        i += 1
    print("Total harvest:", total)
