""" DataRoomCastleTemplate.py """


class DataRoomCastleTemplate:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "castle",
        "description": "You are in a castle",
        "symbol": "⬜",
        'doors': [],
        'room_items': [],
        'extra_items': [
            {
                "name": "floor",
                "description": "You can see a cloudy avatar of yourself in the floor.",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "Not Visible"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "You want to get the floor?"
                    }
                ]
            }
        ],
    }

    def room_data(self):
        """ getter """
        return self._room_data
