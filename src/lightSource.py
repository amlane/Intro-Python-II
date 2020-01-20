from item import Item


class Light(Item):
    def __init__(self, name, description, is_light_on):
        super().__init__(name, description)
        self.is_light_on = is_light_on

    def toggleLight(self):
        self.is_light_on = not self.is_light_on
        if self.is_light_on == True:
            print(f"\nYou turned the {self.name} on")
        else:
            print(f"\nYou turned the {self.name} off")

    def onTake(self):
        print(f"\nYou picked up the {self.name}. \nTry: '{self.name}' to use.")

    def onDrop(self):
        print(f"\nIt's not wise to drop your source of light!")

    def __repr__(self):
        return self.name + " " + self.is_light_on
