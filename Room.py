from helper_functions import print2
from helper_functions import find_item_in_list
from helper_functions import pretty_list


class Room:

    _name = "No name set."
    _description = None
    _items = []
    _doors = []
    _visited = False
    _symbol = "🔲"

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

    def do_look_dir(self, door):
        """ do look dir """

        if not door is None:
            print2(door["description"])
            return

        pd = door["property_dicts"]
        print2("You can't go in that direction.")

    def look_east(self):
        self.do_look_dir(self.eastDoor())

    def look_west(self):
        self.do_look_dir(self.westDoor())

    def look_south(self):
        self.do_look_dir(self.southDoor())

    def look_north(self):
        self.do_look_dir(self.northDoor())

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

    def symbol(self):
        """ getter """
        return self._symbol

    def set_name(self, to_set):
        """ setter """
        self._name = to_set

    def set_description(self, desc):
        """ setter """
        self._description = desc

    def set_doors(self, to_set):
        """ setter """
        self._doors = to_set

    def setVisited(self, to_set):
        """ setter """
        self._visited = to_set

    def set_symbol(self, to_set):
        """ setter """
        self._symbol = to_set
