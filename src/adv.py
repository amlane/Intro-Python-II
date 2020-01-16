import textwrap

from room import Room
from player import Player
from item import Item
from food import Food
from lightSource import Light

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

overlook = room['overlook']
foyer = room['foyer']
outside = room['outside']
treasure = room['treasure']
narrow = room['narrow']

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Player 1", outside)
machete = Item("machete", "a giant machete ax")
axe = Item("axe", "a giant rusty axe")
room['outside'].items = [machete, axe]

apple = Food("apple", "a juicy red delicious", 15)
room['foyer'].items = [apple]

flashlight = Light(
    "flashlight", "a flashlight to guide you through dark rooms", False)
room['overlook'].items = [flashlight]


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print("******************************************************")
print("\n            Welcome to Treasure Hunt 5000! \nGrab items from the rooms as you look for the treasure!")
print("\n********************* DIRECTIONS *********************\n")
print("Select a direction: n, s, e, or w")
print("Check your inventory: i")
print("Check the room for items: c")
print("Pick up an item with 'take' or 'get', Leave an item with 'drop'")
print("Quit game: q")


def changeRoom(direction):
    # checks to make sure
    if hasattr(player.room, direction + "_to"):
        newRoom = getattr(player.room, direction + "_to")
        player.room = newRoom
    else:
        print("\n*** You cannot go this way ***")


    # LOOP
while True:

    str = textwrap.fill(text=player.room.description, width=50)

    # Print current room name
    print(f"\nYou are in the {player.room.name}.")
    print(f"{str}...")
    user_input = input(f"\nWhich direction, {player.name}? ")
    cmd = user_input.split(" ")
    room_items = player.room.items
    inventory = player.items

    if user_input == "n" or user_input == "s" or user_input == "e" or user_input == "w":
        changeRoom(user_input)

    elif user_input == "i":
        print("\nInventory:")
        if len(inventory) == 0:
            print("No items in your inventory")
        for i in range(len(inventory)):
            print(
                f'{i + 1}) {inventory[i].name}: {inventory[i].description}')

    elif user_input == "c":
        print("\nItems in room:")
        # if there are no items in the room
        if len(room_items) == 0:
            print("No items in room\n")
        # prints list of room items
        for i in range(len(room_items)):
            print(
                f"{i + 1}) {room_items[i].name}: {room_items[i].description}")

    elif len(cmd) == 2 and cmd[0] == "get" or cmd[0] == "take":
        userCurrentListLength = len(inventory)
        # check that item exists in the players current room
        for item in room_items:
            # if it does, add the item to the players items and remove it from the room items
            if item.name == cmd[1]:
                inventory.append(item)
                room_items.remove(item)
                item.onTake()
        # if it doesn't, return an error message
        if userCurrentListLength == len(inventory):
            print(f"\nNo {cmd[1]} in this room.")

    elif len(cmd) == 2 and cmd[0] == "drop":
        userCurrentListLength = len(inventory)
        # check that item exists in the players current room
        for item in inventory:
            # if it does, add the item to the players items and remove it from the room items
            if item.name == cmd[1]:
                player.room.items.append(item)
                inventory.remove(item)
                item.onDrop()
        # if it doesn't, return an error message
        if userCurrentListLength == len(inventory):
            print(f"\nThere is no {cmd[1]} in your inventory.")

    elif len(cmd) == 3 and cmd[0] == "turn":
        flashlight.toggleLight()
    elif user_input == "q":
        print("Goodbye")
        break

    else:
        print("\nInvalid selection.")
