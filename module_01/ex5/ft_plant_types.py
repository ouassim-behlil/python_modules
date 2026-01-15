class Plant:
    def __init__(
            self,
            name: str,
            height: int,
            age: int
    ):
        self.name = name
        self._height = height
        self._age = age


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str
    ):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = 3 * self.trunk_diameter // 2
        print(
            f"{self.name.capitalize()}",
            f"provides {shade_area} square meters of shade"
        )


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_saison: str,
            nutritional_value: str
    ):
        super().__init__(name, height, age)
        self.harvest_saison = harvest_saison
        self.nutritional_value = nutritional_value

    def get_nutritional_value(self):
        print(f"{self.name.capitalize()} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    # Flowers
    flower1 = Flower("rose", 60, 1, "red")
    flower2 = Flower("tulip", 45, 1, "yellow")

    flower1.bloom()
    flower2.bloom()

    # Trees
    tree1 = Tree("oak", 500, 10, 50)
    tree2 = Tree("olive", 350, 8, 30)

    tree1.produce_shade()
    tree2.produce_shade()

    # Vegetables
    vegetable1 = Vegetable("carrot", 30, 1, "spring", "vitamin A")
    vegetable2 = Vegetable("spinach", 40, 1, "winter", "iron")

    vegetable1.get_nutritional_value()
    vegetable2.get_nutritional_value()
