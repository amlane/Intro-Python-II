from item import Item


class Zombie(Item):
    def __init__(self, name, description, size, power):
        super().__init__(name, description)
        self.size = size
        self.power = power

    def attack(self):
        print(f"\nYou take a risk and attack {self.name}")

    def dies(self):
        print("****************************************")
        print("****************************************")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***           You killed             ***")
        print(f"                  {self.name}          ")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("****************************************")
        print("****************************************")

    def __repr__(self):
        return self.name + " Class"
