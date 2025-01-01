""" DataRoomBasic.py """


class DataRoomBasic:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "basic room",
        "description": "You are in the most basic room imaginable. Absolutely nothing memorable about this room.",
        'doors':
        [
            {
                "direction": "e",
                'description': "Through an extremely basic opening to the east you feel a basic breeze.",
            }
        ],
        'room_items':
        [
            {
                "name": "candle",
                "visiblePhrase": "A lone, nay lonely, candle waits on a shelf."
            },
        ],
        'extra_items':
        [
            {
                "name": "treasure sign",
                "description": "It says \"DROP *** TREASURE *** HERE\".",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "A wooden sign is planted conspicuously in one corner."
                    },
                    {
                        "gettable": False,
                        "getPhrase": "It's firmly planted in the ground."
                    }
                ]
            }
        ],
    }

    def room_data(self):
        """ getter """
        return self._room_data
