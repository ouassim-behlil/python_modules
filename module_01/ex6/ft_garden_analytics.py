class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        age: int
    ):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(
        self,
        height: int
    ):
        if height < 0:
            print(
                "Height cannot be negative!",
                "\nHeight is set to 0."
            )
            return
        self.__height = height

    def set_age(
        self,
        age: int
    ):
        if age < 0:
            print(
                "Age cannot be negative!",
                "\nAge is set to 0"
            )
            return
        self.__age = age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def grow(self):
        self.__height += 1

    def describe(self) -> str:
        return f"{self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
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
        print(f"{self.name} is blooming!")

    def describe(self) -> str:
        base = super().describe()
        return f"{base}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int
    ):
        super().__init__(name, height, age, color)
        self.__prize_points = 0
        self.set_prize_points(prize_points)

    def set_prize_points(
        self,
        prize_points: int
    ):
        if prize_points < 0:
            print("Prize points cannot be negatives!")
            print("They are set to default: 0")
            return
        self.__prize_points = prize_points


    def get_prize_points(self) -> int:
        return self.__prize_points

    def describe(self) -> str:
        """
        describes the prize flower.

        Args:
        self: instance of the class.

        Returns:
        str: string describing the prizeflower plant.
        """
        base = super().describe()
        return f"{base}, Prize points: {self.get_prize_points()}"


class GardenManager:
    def __init__(self):
        """
        Default constructor of the class.
        """
        self.gardens = {}

    def add_plant(
        self,
        owner: str,
        plant: Plant
    ):
        """
        Add plant to the owner garden

        Args:
        self: instance of the class
        string: owner of garden
        Plant: instance of Plant
        """
        if owner not in self.gardens.keys():
            self.gardens[owner] = []
        self.gardens[owner].append(plant)
    
    def simulate_growth(
        self,
        owner: Plant
    ):
        """
        This method simulates growth of plants of the owner

        Args:
        self: instance of class
        string: owner of the garden
        """
        if owner not in gardens.keys():
            print("Owner has no plants!")
            return
        print(f"{owner.capitalize()} is helping all plants grow...")
        for plant in gardens[owner]:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    @classmethod
    def create_garden_network(cls) -> GardenManager:
        """
        class method to create a pre-configured garden manager with demo gardens.

        Args:
        cls: the class

        Returns:
        GardenManager: a garden manager with Alice's and Bob's gardens.
        """
        manager = cls()

        # Alice Garden:
        oak = Plant("Oak Tree", 100, 365)
        rose = FloweringPlant("Rose", 25, 30, "red")
        sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

        manager.add_plant("Alice", oak)
        manager.add_plant("Alice", rose)
        manager.add_plant("Alice", sunflower)

        # Bob Garden
        fern = Plant("Fern", 40, 90)
        daisy = FloweringPlant("Daisy", 20, 25, "white")

        manager.add_plant("Bob", fern)
        manager.add_plant("Bob", daisy)

        return manager
    
    @staticmethod
    def validate_height(height: int) -> bool:
        """
        static method that takes height as integer and checks if it's valid.

        Args:
        int: height of the plant

        Returns:
        bool: True if height is valid, False otherwise
        """
        if height < 0:
            return False
        return True

    
