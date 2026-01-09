class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = 0
        self.__age = 0
        print("Plant created:", name)
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int):
        if height < 0:
            print("Negative height rejected!")
            return
        self.__height = height
        print(f"Height updated: {height}cm [ok]")

    def set_age(self, age: int):
        if age < 0:
            print("Age must be positive!")
            return
        self.__age = age
        print(f"age updated: {age} [ok]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def print_info(self):
        print(f"Current plant: {self.name} ({self.get_height()}cm,\
        {self.get_age()} days)")


if __name__ == "__main__":
    rose_plant = SecurePlant("rose", 25, 30)

    rose_plant.set_height(-6)
    rose_plant.print_info()
