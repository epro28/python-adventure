""" DataRoomBlueRoom.py """


class DataRoomBlueRoom:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "template": "castle",
        "name": "blue room",
        "description": "The first thing you notice when you step into the room are the royal blue curtains that frame \
            the window. They're matched by a cerulean woven rug spread across the floor, and an azure-patterned wallpaper. \
                As you look around, you realize almost every accent of this room is a different but matching shade of blue.",
        'doors':
        [
            {
                "direction": "e",
                "description": "TODO",
                "property_dicts": [
                    {
                        "passable": False,
                        "passPhrase": "TODO: No room here yet"
                    }
                ]
            },
            {
                "direction": "w",
                "description": "There is only an unoccupied wallpapered wall.",
                "property_dicts": [
                    {
                        "passable": False,
                        "passPhrase": "There's nowhere to go in that direction."
                    }
                ]
            },
            {
                "direction": "s",
                "description": "A hallway extends to the south.",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "n",
                "description": "You see a window framed by royal blue curtains.",
                "property_dicts": [
                    {
                        "passable": False,
                        "passPhrase": "There's nowhere to go in that direction."
                    }
                ]
            }
        ],
        'extra_items':
        [
            {
                "name": "royal blue curtains",
                "description": "Long blue curtains made of a thick luxurious fabric.",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "not visible"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "They're firmly fastened to the window."
                    },
                    {
                        "opened": False,
                        "desc": "Long blue curtains made of a thick luxurious fabric.",
                        "revealedItem": {
                            "name": "sapphire egg",
                            "revealedPhrase": "Pushing the curtains back reveals a \
                                beautiful sapphire egg resting in the corner of the the window."
                        }
                    }
                ]
            },
            {
                "name": "cerulean woven rug",
                "description": "A handsome handwoven rug of thick cerulean fibers.",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "not visible"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "It's much too heavy to carry."
                    },
                    # {
                    #    "moved": False,
                    #    "desc": "A handsome handwoven rug of thick cerulean fibers.",
                    #    "revealedItem": {
                    #        "name": "sapphire egg",
                    #        "revealedPhrase": "Lifting the corner of the rug reveals a beautiful egg made of sapphire."
                    #    }
                    # }
                ]
            }
        ],
        'room_items': [],
    }

    def room_data(self):
        """ getter """
        return self._room_data
