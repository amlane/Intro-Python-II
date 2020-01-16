# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, is_light):
        self.name = name
        self.description = description
        self.items = []
        self.is_light = is_light

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def __repr__(self):
        return self.name + " Class"
