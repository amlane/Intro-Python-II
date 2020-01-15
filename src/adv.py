import textwrap

from room import Room
from player import Player
from item import Item

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
room['outside'].items = [machete.name]


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


print("Welcome to the game! \nGrab items in the room and look for the treasure!")


def changeRoom(direction):
    # checks to make sure
    if hasattr(player.room, direction + "_to"):
        newRoom = getattr(player.room, direction + "_to")
        player.room = newRoom
    else:
        print("\n*** You cannot go this way ***")


def pickUpItem(index):
    item = player.room.items[index - 1]
    if item:
        print("item exists")
        player.items.append(item)
        player.room.items.remove(item)
    else:
        print("item doesn't exist")

    # LOOP
while True:

    str = textwrap.fill(text=player.room.description, width=50)

    # Print current room name
    print(f"\nYou are in the {player.room.name}.")
    print(f"{str}...")
    user_input = input(f"\nWhich direction, {player.name}? ")

    if user_input == "q":
        print("Goodbye")
        break
    elif "n" in user_input or "s" in user_input or "e" in user_input or "w" in user_input:
        changeRoom(user_input)
    elif user_input == "i":
        print("\nInventory:")
        if len(player.items) == 0:
            print("No items in your inventory")
        for i in range(len(player.items)):
            print(f'{i + 1}) {player.items[i]}')
    elif user_input == "c":
        print("\nItems in room:")
        if len(player.room.items) == 0:
            print("No items in room")
        for i in range(len(player.room.items)):
            print(f"{i + 1}) {player.room.items[i]}")
            item_input = int(input("Pick up an item by entering the number: "))
            pickUpItem(item_input)
    else:
        print("\nInvalid selection.\n")
