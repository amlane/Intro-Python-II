# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def setRoom(self, newRoom):
        self.room = newRoom

    def __repr__(self):
        return self.name
