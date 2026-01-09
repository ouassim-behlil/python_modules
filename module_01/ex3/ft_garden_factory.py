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


class Plant_factory:
    def __init__(self):
        self.plants = []
        self.count = 0

    def create_plant(self, name: str, height: int, age: int):
        plant = Plant(name, height, age)
        self.plants.append(plant)
        self.count += 1
        print(f"Created: {name.capitalize()} ({height}cm, {age}) days")


if __name__ == "__main__":
    factory = Plant_factory()

    print("=== Plant Factory Output ===")

    factory.create_plant("rose", 25, 30)
    factory.create_plant("oak", 200, 365)
    factory.create_plant("cactus", 5, 90)
    factory.create_plant("sunflower", 80, 45)
    factory.create_plant("fern", 15, 120)

    print("Total plants created:", factory.count)
