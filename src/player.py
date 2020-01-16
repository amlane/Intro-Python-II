# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room):
        self.name = name  # string
        self.room = room  # class
        self.life = 15  # int
        self.items = []  # list

    def travelRooms(self, room, direction):
        if getattr(room, f"{direction}_to") != None:
            newRoom = getattr(room, f"{direction}_to")
            self.room = newRoom
        else:
            print("\n*** You cannot go this way ***")

    def attack(self, zombie):
        print(
            f"\n{self.name.capitalize()} reached up with their weapon and attacked {zombie.capitalize()}.")

    def dies(self):
        print("****************************************")
        print("****************************************")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***          You're dead.            ***")
        print("***        Play again(y/n)?          ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("****************************************")
        print("****************************************")

    def __repr__(self):
        return self.name + " Class"
