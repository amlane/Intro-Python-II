# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, is_light, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light

    def __repr__(self):
        return self.name + " Class"
