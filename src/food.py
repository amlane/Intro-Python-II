from item import Item


class Food(Item):
    def __init__(self, name, description, energy):
        super().__init__(name, description)
        self.energy = energy

    def eat(self):
        print(f"\nYou ate the {self.name}. Yum!")

    def __repr__(self):
        return f"{self. name} {self. energy}"
