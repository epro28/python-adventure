""" DataRoomBlueRoom.py """


class DataRoomBlueRoom:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "template": "castle",
        "name": "blue room",
        "description": "The first thing you notice when you enter are the closed royal blue curtains that frame \
            the window. They're matched by a cerulean woven rug spread across the floor and an azure patterned wallpaper. \
                As you survey the room, you realize almost every accent in this room is a different but matching shade of blue.",
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
                "name": "cerulean rug",
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
                ]
            },
            {
                "name": "azure wallpaper",
                "description": "The interchanging diagonal lines give the room a modern feel.",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "not visible"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "It's plastered on and not coming off any time soon."
                    },
                    {
                        "looked": False,
                        "desc": "The interchanging diagonal lines give the room a modern feel.",
                        "revealedItem": {
                            "name": "faint scribblings",
                            "revealedPhrase": "After staring at the wallpaper for some time you start to notice some\
                                faint scribblings."
                        }
                    },
                ]
            },
            {
                "name": "faint scribblings",
                "description": "A little lower than eye-level you can make out a string of letters handwritten on the \
                    wall. A. K. A. R. U. I. Is that... Japanese?",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "You can barely make out some faint scribblings on the wall."
                    },
                    {
                        "gettable": False,
                        "getPhrase": "Read them, and you can carry them in your head."
                    },
                ]
            },
        ],
        'room_items': [],
    }

    def room_data(self):
        """ getter """
        return self._room_data
