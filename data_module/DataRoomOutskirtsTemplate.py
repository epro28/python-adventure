""" DataRoomOutskirtsTemplate.py """


class DataRoomOutskirtsTemplate:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "outskirts",
        "description": "You are on the outskirts",
        "symbol": "🟩",
        'doors': [],
        'room_items': [],
        'extra_items': [],
    }

    def room_data(self):
        """ getter """
        return self._room_data
