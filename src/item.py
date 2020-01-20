class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def onTake(self):
        print(f"\nYou have picked up the {self.name}.")

    def onDrop(self):
        print(f"\nYou dropped the {self.name}.")

    def __repr__(self):
        return self.name + " Class"
