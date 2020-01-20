from item import Item


class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def __repr__(self):
        return f"{self.name} {self.damage}"
