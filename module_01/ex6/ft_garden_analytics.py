class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        age: int
    ):

        """ Default Constructor"""
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(
        self,
        height: int
    ) -> None:
        """ Validates height before update the instance height variable. """

        if height < 0:
            self.__height = 0
            print(
                "Height cannot be negative!",
                "\nHeight is set to 0."
            )
            return
        self.__height = height

    def set_age(
        self,
        age: int
    ) -> None:
        """ Validate Age before update the instance age variable. """

        if age < 0:
            print(
                "Age cannot be negative!",
                "\nAge is set to 0"
            )
            return
        self.__age = age

    def get_height(self) -> int:
        """ Get the height of the instance"""
        return self.__height

    def get_age(self) -> int:
        """ Get the age of the instance"""
        return self.__age

    def grow(self) -> None:
        """ Increment the height of the instance by 1"""
        self.__height += 1

    def describe(self) -> str:
        """
        Describe the instance.

        Returns:
            string describing the instance
        """
        return f"- {self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str
    ):
        """ Default Constructor """

        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming!")

    def describe(self) -> str:
        """
        Describe the Flower

        Args:
            self: the instance.

        Returns:
            a string describing the instance.
        """
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
        """
            Default constructor
        """
        super().__init__(name, height, age, color)
        self.set_prize_points(prize_points)

    def set_prize_points(
        self,
        prize_points: int
    ):
        """ Validate the prize points before update."""

        if prize_points < 0:
            self.__prize_points = 0
            print("Prize points cannot be negatives!")
            print("It is set to default: 0")
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
        self.stats = {}

    def add_plant(
        self,
        owner: str,
        plant: Plant
    ) -> None:
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
        print(f"Added {plant.name} to {owner}'s garden")

        if owner not in self.stats.keys():
            self.stats[owner] = GardenManager.GardenStats()
        self.stats[owner].total_plants += 1

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
        if owner not in self.gardens.keys():
            print("Owner has no plants!")
            return
        print(f"\n{owner.capitalize()} is helping all plants grow...")
        for plant in self.gardens[owner]:
            plant.grow()
            print(f"{plant.name} grew 1cm")

        self.stats[owner].total_growth += len(self.gardens[owner])

    def garden_report(self, owner: str) -> None:
        if owner not in self.gardens.keys():
            print(f"{owner} has no garden yet")
            return
        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden")
        for plant in self.gardens[owner]:
            print(plant.describe())
        print(
            f"\n Plants added: {self.stats[owner].total_plants},",
            f"Total growth: {self.stats[owner].total_growth}"
              )
        count = self.stats[owner].count_plants_by_type(self.gardens[owner])
        print(
            "Plant types:",
            f"{count['regular']} regular, "
            f"{count['flowering']} flowering, "
            f"{count['prize_flowers']} prize flowers\n"
        )

    def manager_report(self) -> None:
        print(
            "Height validation test: ",
            GardenManager.GardenStats.height_validation_test(self.gardens),
            )
        print("Garden scores -", end="")
        scores = GardenManager.GardenStats.garden_scores(self.gardens)
        for owner, score in scores.items():
            print(f" {owner}: {score},", end='')

        print("\nTotal gardens managed:", len(self.gardens))

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """
        class method to create a pre-configured
        garden manager with demo gardens.

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

    class GardenStats:
        def __init__(self):
            self.total_growth = 0
            self.total_plants = 0

        @staticmethod
        def count_plants_by_type(garden: list[Plant]) -> dict[str, int]:
            """
            Count the plants of a garden by Plant type.

            Args:
                garden (list): list of plants

            Returns:
                count (Dict): a dictionary with type as key and count as value
            """
            count = {
                'regular': 0,
                'flowering': 0,
                'prize_flowers': 0
            }
            for plant in garden:
                if isinstance(plant, PrizeFlower):
                    count['prize_flowers'] += 1
                elif isinstance(plant, FloweringPlant):
                    count['flowering'] += 1
                else:
                    count['regular'] += 1
            return count

        @staticmethod
        def height_validation_test(gardens: dict[str, list[Plant]]) -> bool:
            """
            Check the height of all plants:

            Args:
               gardens (dict): dict of gardens with onwers as keys.

            Returns:
                bool: True if height in all plants is valid
            """
            for garden in gardens.values():
                for plant in garden:
                    if plant.get_height() < 0:
                        return False
            return True

        @staticmethod
        def garden_scores(gardens: dict[str, list[Plant]]) -> dict[str, int]:
            """
            Docstring for garden_scores

            :param gardens: gardens
            :type gardens: dict[str, list[Plant]]
            :return: score for each owner in the garden manager
            :rtype: dict[str, int]
            """
            scores = {}
            for owner, garden in gardens.items():
                score = len(garden) * 88
                scores[owner] = score
            return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    manager.simulate_growth('Alice')
    manager.garden_report('Alice')
    manager.manager_report()
