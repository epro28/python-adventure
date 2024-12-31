""" Inventory.py """
from helper_functions import print2
from helper_functions import find_item_in_list
from helper_functions import pretty_list


class Inventory:
    
    """ The player's inventory """
    _items = []

    def __init__(self):
        self._items = []

    def add(self, item):
        """ add """
        self._items.append(item)

    def remove(self, item):
        """ remove """
        self._items.remove(item)

    def find(self, thing_name_to_find):
        """ return item if found; otherwise return None """
        item = find_item_in_list(thing_name_to_find, self._items)
        return item

    def look(self):
        """ look """
        if len(self._items) > 0:
            print2(pretty_list("You are carrying ", self._items))
        else:
            print2("You have no things. You must get the things.")
