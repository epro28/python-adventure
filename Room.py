from helper_functions import print2
from helper_functions import find_item_in_list
from helper_functions import pretty_list


class Room:

    _name = "No name set."
    _description = None
    _items = []
    _doors = []
    _visited = False

    def __init__(self, name):
        self._name = name
        self._description = "This room's description has not been set."
        self._items = []
        self._doors = []
        self._visited = False

    def add_item(self, item):
        """ add item to room """
        self._items.append(item)

    def removeItem(self, itemName):
        for item in self._items:
            if item.name() == itemName:
                self._items.remove(item)
                return
        print("!!! Item to remove not found")
        return

    def find(self, thing_name_to_find):
        """ return item if found; otherwise return None """
        item = find_item_in_list(thing_name_to_find, self._items)
        return item

    def has_item(self, item_name):
        """ True is the item is in the room; otherwise False """
        if self.find(item_name) is None:
            return False
        return True

    def look(self):
        """ Handle look """
        to_print = self._description

        items_on_floor = []
        for item in self._items:
            if item.get_property("visiblePhrase") == "":
                items_on_floor.append(item)
            else:
                if item.get_property("visible"):
                    to_print = to_print + " " + \
                        item.get_property("visiblePhrase")
        print2(to_print)

        if len(items_on_floor) > 0:
            print2(pretty_list("On the floor you see ", items_on_floor))

        # print list of items in room
        # if len(self._items) > 0:
        #    print("(Debug) Items in room: ")
        #    to_print = ""
        #    for item in self._items:
        #        to_print = to_print + item.pretty_name() + ", "
        #    to_print = to_print[:-2]  # remove the ", " from the last item
        #    print(to_print)

    def doLookDir(self, door):
        if not door is None:
            print2(door["description"])
        else:
            print2("You can't go in that direction.")

    def lookEast(self):
        self.doLookDir(self.eastDoor())

    def lookWest(self):
        self.doLookDir(self.westDoor())

    def lookSouth(self):
        self.doLookDir(self.southDoor())

    def lookNorth(self):
        self.doLookDir(self.northDoor())

    # Getters
    def name(self):
        """ getter """
        return self._name

    def items(self):
        """ getter """
        return self._items

    def eastDoor(self):
        for door in self._doors:
            if door["direction"] == "e":
                return door
        return None

    def westDoor(self):
        for door in self._doors:
            if door["direction"] == "w":
                return door
        return None

    def southDoor(self):
        for door in self._doors:
            if door["direction"] == "s":
                return door
        return None

    def northDoor(self):
        for door in self._doors:
            if door["direction"] == "n":
                return door
        return None

    def visited(self):
        return self._visited

        # Setters
    def set_description(self, desc):
        self._description = desc

    def setDoors(self, to_set):
        self._doors = to_set

    def setVisited(self, to_set):
        self._visited = to_set
