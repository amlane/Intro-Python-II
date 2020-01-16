# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room, life=1, items=[]):
        self.name = name  # string
        self.room = room  # class
        self.life = life  # int
        self.items = items  # list

    def dies(self, startingRoom):
        print("****************************************")
        print("****************************************")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***          You're dead.            ***")
        print("***         Play again(y/n)?         ***")
        print("***                                  ***")
        print("***                                  ***")
        print("***                                  ***")
        print("****************************************")
        print("****************************************")

    def __repr__(self):
        return self.name + " Class"
