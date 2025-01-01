""" DataRoomFrontDoor.py """


class DataRoomFrontDoor:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "front door",
        "description": "The dirt path from the north stops here. To the east is\
              a large wooden door. The forest is to the west. The stone building's \
                wall extends further to the south.",
        'doors':
        [
            {
                "direction": "e",
                "description": "TODO: a wooden door.",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "w",
                "description": "There's a dense forest to the west.",
                "property_dicts": [
                    {
                        "passable": False,
                        "passPhrase": "You have no desire to re-enter the forest at this point."
                    }
                ]
            },
            {
                "direction": "s",
                "description": "The stone building's wall extends further to \
                    the south.",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "n",
                "description": "The dirt path leads to the north",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            }
        ],
        'room_items':
        [],
        'extra_items':
        [
            {
                "name": "wooden door",
                "description": "TODO: a large wooden door.",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "TODO: Its large and wooden."
                    },
                    {
                        "gettable": False,
                        "getPhrase": "Yeh right."
                    }
                ]
            }
        ],
    }

    def room_data(self):
        """ getter """
        return self._room_data
