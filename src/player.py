# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name  # string
        self.room = room  # class

    def __repr__(self):
        return self.name + " Class"
