class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class GardenManager:
    def __init__(self):
        self.plants = []
        self.tank = 2

    def add_plant(self, plant_name, water_level, sun_light):
        try:
            if plant_name is None or plant_name == "":
                raise PlantError("Plant name cannot be empty or None!")
            self.plants.append({
                 'name': plant_name,
                 'water_level': water_level,
                 'sun_light': sun_light
            })
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print("Error adding plant:", e)

    def watering_plants(self):
        try:
            for plant in self.plants:
                if self.tank < 1:
                    raise WaterError("Not enough water in tank")
                plant['water_level'] += 1
                self.tank -= 1
                print(f"Watering {plant['name']} - success")
        except (ValueError, KeyError) as e:
            print("Caught an error:", e)
        except GardenError as e:
            print("Caught GardenError:", e)
        finally:
            print("Closing watering system (cleanup)")

    def chack_plant_health(self):
        try:
            for plant in self.plants:
                if plant['water_level'] > 10:
                    raise ValueError(f"Water level {plant['water_level']}"
                                     " is too high (max 10)")

                if plant['water_level'] < 1:
                    raise ValueError(f"Water level {plant['water_level']}"
                                     " is too low (min 1)")

                if plant['sun_light'] < 2:
                    raise ValueError(f"Sunlight hours {plant['sun_light']}"
                                     " is too low (min 2)")

                if plant['sun_light'] > 12:
                    raise ValueError(f"Sunlight hours {plant['sun_light']}"
                                     " is too high (min 12)")
                print(f"{plant['name']}: healthy (water: "
                      f"{plant['water_level']}, sun: {plant['sun_light']})")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    manager = GardenManager()

    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    manager.add_plant('tomatos', 4, 5)
    manager.add_plant('lettuce', 3, 19)
    manager.add_plant('', 4, 7)

    print("\nWatering plants...")
    manager.watering_plants()

    print("\nChecking plant health...")
    manager.chack_plant_health()

    print("\nTesting error recovery...")
    manager.watering_plants()

    print("\nGarden management system test complete!")
