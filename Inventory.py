from helper_functions import print2
from helper_functions import find_item_in_list


class Inventory:

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
            print2("You are carrying: ")
            to_print = ""
            for item in self._items:
                to_print = to_print + item.pretty_name() + ", "
            to_print = to_print[:-2]  # remove the ", " from the last item
            print2(to_print)
        else:
            print2("You have no things.")
