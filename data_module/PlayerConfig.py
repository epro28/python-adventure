""" PlayerConfig.py """


class PlayerConfig:  # pylint: disable=too-few-public-methods
    """ Inventory """
    _inventory_items = []
    _position_x = 0
    _position_y = 1

    def inventory_items(self):
        """ getter """
        return self._inventory_items

    def position(self):
        """ getter """
        return self._position_x, self._position_y
