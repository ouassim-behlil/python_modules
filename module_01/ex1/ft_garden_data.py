class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def display_plant_info(self):
        print(f"{self.name.capitalize()}: \
        {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 100)
    sunflower = Plant("sunflower", 15, 25)
    cactus = Plant("cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.display_plant_info()
    sunflower.display_plant_info()
    cactus.display_plant_info()
