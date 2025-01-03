""" DataRoomCastleTemplate.py """


class DataRoomCastleTemplate:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "castle",
        "description": "You are in a castle",
        "symbol": "⬜",
        'doors': [],
        'room_items': [],
        'extra_items': [],
    }

    def room_data(self):
        """ getter """
        return self._room_data
