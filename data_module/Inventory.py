""" Inventory.py """


class Inventory:  # pylint: disable=too-few-public-methods
    """ Inventory """
    _inventory_items = []

    def inventory_items(self):
        """ getter """
        return self._inventory_items
