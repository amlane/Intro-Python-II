# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name  # string
        self.room = room  # class
        self.items = items  # list

    def __repr__(self):
        return self.name + " Class"
