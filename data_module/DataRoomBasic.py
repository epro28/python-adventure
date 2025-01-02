""" DataRoomBasic.py """


class DataRoomBasic:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "basic room",
        "description": "You are in the most basic room imaginable. Absolutely nothing memorable about this room.",
        "symbol": "⬜",
        'doors':
        [
            {
                "direction": "e",
                "description": "TODO",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "w",
                "description": "TODO",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "s",
                "description": "TODO",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "n",
                "description": "TODO",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
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
