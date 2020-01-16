from item import Item


class Food(Item):
    def __init__(self, name, description, energy):
        super().__init__(name, description)
        self.energy = energy

    def __repr__(self):
        return self.name + " " + self.energy
