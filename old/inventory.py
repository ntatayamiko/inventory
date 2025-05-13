import os
import sqlite3
import gui


class Livestock:
    def __init__(self, animal_id, breed, age, weight, health_status):
        self.animal_id = animal_id
        self.breed = breed
        self.age = age
        self.weight = weight
        self.health_status = health_status

    def __repr__(self):
        return (f"ID: {self.animal_id}, Breed: {self.breed}, "
                f"Age: {self.age} years, Weight: {self.weight} kg, "
                f"Health: {self.health_status}")


class LivestockInventory:
    def __init__(self):
        self.animals = {}

    def add_animal(self, animal_id, breed, age, weight, health_status):
        if animal_id in self.animals:
            print("Error: Animal ID already exists.")
            return False
        self.animals[animal_id] = Livestock(animal_id, breed, age, weight, health_status)
        return True

    def update_animal(self, animal_id, breed=None, age=None, weight=None, health_status=None):
        if animal_id not in self.animals:
            print("Error: Animal ID not found.")
            return False
        animal = self.animals[animal_id]
        if breed is not None:
            animal.breed = breed
        if age is not None:
            animal.age = age
        if weight is not None:
            animal.weight = weight
        if health_status is not None:
            animal.health_status = health_status
        return True

    def remove_animal(self, animal_id):
        if animal_id not in self.animals:
            print("Error: Animal ID not found.")
            return False
        del self.animals[animal_id]
        return True

    def search_animals(self, breed=None, health_status=None):
        results = []
        for animal in self.animals.values():
            if breed and animal.breed != breed:
                continue
            if health_status and animal.health_status != health_status:
                continue
            results.append(animal)
        return results

    def generate_inventory_report(self):
        print("\nFull Inventory Report:")
        for animal in self.animals.values():
            print(animal)

    def generate_health_report(self):
        health_counts = {}
        for animal in self.animals.values():
            status = animal.health_status
            health_counts[status] = health_counts.get(status, 0) + 1
        print("\nHealth Status Report:")
        for status, count in health_counts.items():
            print(f"{status}: {count} animals")

    def generate_breed_report(self):
        breed_stats = {}
        for animal in self.animals.values():
            breed = animal.breed
            if breed not in breed_stats:
                breed_stats[breed] = {'count': 0, 'total_weight': 0}
            breed_stats[breed]['count'] += 1
            breed_stats[breed]['total_weight'] += animal.weight

        print("\nBreed Statistics Report:")
        for breed, stats in breed_stats.items():
            avg_weight = stats['total_weight'] / stats['count']
            print(f"{breed}: {stats['count']} animals, Average Weight: {avg_weight:.2f} kg")


def main():
    inventory = LivestockInventory()

    while True:
        print("\nLivestock Inventory Management System")
        print("1. Add Animal")
        print("2. Update Animal Details")
        print("3. Remove Animal")
        print("4. Search Animals")
        print("5. Generate Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            animal_id = input("Enter animal ID: ")
            breed = input("Enter breed: ")
            age = input("Enter age (years): ")
            weight = input("Enter weight (kg): ")
            health_status = input("Enter health status: ")

            try:
                age = float(age)
                weight = float(weight)
                if inventory.add_animal(animal_id, breed, age, weight, health_status):
                    print("Animal added successfully.")
            except ValueError:
                print("Invalid age or weight. Please enter numbers.")

        elif choice == '2':
            animal_id = input("Enter animal ID to update: ")
            if animal_id not in inventory.animals:
                print("Animal not found.")
                continue

            breed = input("Enter new breed (leave blank to keep current): ").strip()
            breed = breed if breed else None

            age = None
            age_input = input("Enter new age (years) (leave blank to keep current): ").strip()
            if age_input:
                try:
                    age = float(age_input)
                except ValueError:
                    print("Invalid age input. Age not updated.")

            weight = None
            weight_input = input("Enter new weight (kg) (leave blank to keep current): ").strip()
            if weight_input:
                try:
                    weight = float(weight_input)
                except ValueError:
                    print("Invalid weight input. Weight not updated.")

            health_status = input("Enter new health status (leave blank to keep current): ").strip()
            health_status = health_status if health_status else None

            if inventory.update_animal(animal_id, breed, age, weight, health_status):
                print("Animal details updated.")

        elif choice == '3':
            animal_id = input("Enter animal ID to remove: ")
            if inventory.remove_animal(animal_id):
                print("Animal removed successfully.")

        elif choice == '4':
            breed = input("Enter breed to filter (leave blank for all): ").strip()
            health_status = input("Enter health status to filter (leave blank for all): ").strip()
            results = inventory.search_animals(
                breed=breed if breed else None,
                health_status=health_status if health_status else None
            )
            print(f"\nFound {len(results)} animals:")
            for animal in results:
                print(animal)

        elif choice == '5':
            print("\nReport Options:")
            print("1. Full Inventory Report")
            print("2. Health Status Report")
            print("3. Breed Statistics Report")
            report_choice = input("Enter report choice: ")

            if report_choice == '1':
                inventory.generate_inventory_report()
            elif report_choice == '2':
                inventory.generate_health_report()
            elif report_choice == '3':
                inventory.generate_breed_report()
            else:
                print("Invalid report choice.")

        elif choice == '6':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
