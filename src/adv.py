import textwrap
import random

from room import Room
from player import Player
from item import Item
from food import Food
from lightSource import Light
from zombie import Zombie
from weapon import Weapon

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", True),
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
player = Player(input("Enter your name -> ").capitalize(), outside)
machete = Weapon("machete", "a giant machete ax", 15)
axe = Weapon("axe", "a giant rusty axe", 8)
apple = Food("apple", "a juicy red delicious", 15)
flashlight = Light(
    "flashlight", "A flashlight to guide you through dark rooms. \n* Use with the [flashlight] command", False)
joe = Zombie(
    "Joe", "A lurker zombie. \nUse [attack] command with my name.", "medium", 20)
steve = Zombie(
    "Steve", "A dumb zombie. \nUse [attack] command with my name.", "large", 18)
bob = Zombie(
    "Bob", "A big zombie. \nUse [attack] command with my name.", "x-large", 23)


room['outside'].items = [machete, axe, steve, bob]
room['foyer'].items = [apple]
room['overlook'].items = [flashlight]
room['narrow'].items = [joe]


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
print("Check your inventory: i or inventory")
print("Check the room for items: c or check")
print("Other available commands: take, get, attack and eat [item]")
print("Quit game: q")

directions = ["n", "s", "e", "w"]

# LOOP
while True:
    room_items = player.room.items
    inventory = player.items
    weapons = [w for w in inventory if hasattr(w, "damage")]
    food = [f for f in inventory if hasattr(f, "energy")]
    monsters = [m for m in room_items if hasattr(m, "power")]

    # If the play is dead ask if they want to restart the game or quit the game
    if player.life <= 0:
        player.dies()
        x = input("-> ")
        if x == "y":
            player.room = outside
            player.life = 15
            player.items = []
            room['outside'].items = [machete, axe]
            room['foyer'].items = [apple]
            room['overlook'].items = [flashlight]
            room['narrow'].items = [joe]
            continue
        elif x == "n":
            print("Press q to exit the game.")
    # checks if flashlight is on

    def is_flashlight_on():
        result = 0
        for item in inventory:
            if item.name == "flashlight" and item.is_light_on == True:
                result += 1
        if result == 0:
            return False
        else:
            return True

    # Print current room name
    print(f"\nLife: {player.life}")
    print(f"\nYou are in the {player.room.name}.")
    str = textwrap.fill(text=player.room.description, width=50)
    print(f"{str}...")

    user_input = input(f"\nWhich direction, {player.name}? ").lower()

    cmd = user_input.split(" ")

    # CHANGE ROOM
    if user_input in directions:
        player.travelRooms(player.room, user_input)
    # CHECK INVENTORY
    elif user_input == "i" or user_input == "inventory":
        print("\nInventory:")
        if len(inventory) == 0:
            print("No items in your inventory")
        for i in range(len(inventory)):
            print(
                f'{i + 1}) {inventory[i].name}: {inventory[i].description}')
    # CHECK ROOM ITEMS
    elif user_input == "c" or user_input == "check":
        # If lights are on or you have a light source that's on, print a list of items in room
        if player.room.is_light == True or is_flashlight_on():
            print("\nItems in room:")
            # if there are no items in the room
            if len(room_items) == 0:
                print("No items in room\n")
            # prints list of room items
            for i in range(len(room_items)):
                print(
                    f"{i + 1}) {room_items[i].name}: {room_items[i].description}")
        else:
            print("\nYou cannot see the items in this room without a light source!")
    # PICK UP ITEMS
    elif len(cmd) == 2 and cmd[0] == "get" or cmd[0] == "take":
        userCurrentListLength = len(inventory)
        # check if light is on
        if player.room.is_light == True or is_flashlight_on():
            # check that item exists in the players current room
            for item in room_items:
                # if it does, add the item to the players items and remove it from the room items
                if item.name.lower() == cmd[1]:
                    inventory.append(item)
                    room_items.remove(item)
                    item.onTake()
            # if it doesn't, return an error message
            if userCurrentListLength == len(inventory):
                print(f"\nNo {cmd[1]} in this room.")
        else:
            print("\nYou cannot pick up items in this room without a lightsource.")
    # DROP ITEMS
    elif len(cmd) == 2 and cmd[0] == "drop":
        userCurrentListLength = len(inventory)
        # check that item exists in the players current room
        for item in inventory:
            # if it does, add the item to the players items and remove it from the room items
            if item.name.lower() == cmd[1]:
                room_items.append(item)
                inventory.remove(item)
                item.onDrop()
        # if it doesn't, return an error message
        if userCurrentListLength == len(inventory):
            print(f"\nThere is no {cmd[1]} in your inventory.")
    # TOGGLE LIGHT
    elif user_input == "flashlight":
        result = 0
        for item in inventory:
            if item.name == "flashlight":
                result += 1
                flashlight.toggleLight()
        if result == 0:
            print("\nYou don't have the flashlight in your inventory.")
    # EAT
    elif len(cmd) == 2 and cmd[0] == "eat":
        result = 0
        for item in food:
            if item.name == cmd[1]:
                result += 1
                item.eat()
                player.life += item.energy
                inventory.remove(item)
        if result == 0:
            print(f"\nYou cannot eat {cmd[1]}.")
    # ATTACK
    elif len(cmd) == 2 and cmd[0] == "attack":
        player.attack(cmd[1])
        randomNum = random.randint(0, 15)
        result = 0
        for zombie in monsters:
            if zombie.name.lower() == cmd[1]:
                result += 1
                if(randomNum >= 10):
                    player.life += randomNum
                    zombie.power -= randomNum
                    print(
                        f"You made a hit! \nYou gained {randomNum} life.")
                    if zombie.power <= 0:
                        zombie.dies()
                        room_items.remove(zombie)
                    else:
                        print(f"{zombie.name} has {zombie.power} power left.")
                else:
                    player.life -= randomNum
                    zombie.power += randomNum
                    print(
                        f"{zombie.name} blocked the blow. \nYou lost {randomNum} life.")
                    print(f"{zombie.name} has {zombie.power} power left.")

        if result == 0:
            print(f"\n'attack {cmd[1]}' is not a valid command.")

    elif user_input == "q":
        print("Goodbye")
        break

    else:
        print("\nInvalid selection.")
