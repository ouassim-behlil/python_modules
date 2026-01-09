class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.days_age = age

    def get_info(self):
        return f"{self.name.capitalize()}: \
        {self.height}cm, {self.days_age} days old"

    def grow(self):
        self.height += 1

    def age(self):
        self.days_age += 1


if __name__ == "__main__":
    rose = Plant("rose", 25, 100)
    sunflower = Plant("sunflower", 15, 25)
    cactus = Plant("cactus", 15, 120)
    plants = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    days = 1
    while days < 8:
        i = 0
        print(f"=== Day {days} ===")
        while i < 3:
            plants[i].age()
            plants[i].grow()
            print(plants[i].get_info())
            i += 1
        days += 1
