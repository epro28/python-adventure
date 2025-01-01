""" DataRoomStudy.py """


class DataRoomStudy:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "study",
        "description": "You are in a cozy study. In the middle of the room is a large oak\
              desk surrounded by floor-to-ceiling bookshelves on every wall. A well-worn \
                chair rests before a stack of books.",
        'doors':
        [
            {
                "direction": "e",
                'description': "Through an extremely basic opening to the east you feel a\
                      basic breeze.",
            }
        ],
        'room_items':
        [
            {
                "name": "red book",
                "visiblePhrase": "On the table lies a closed brown-leather book with red accents."
            },
            {
                "name": "amethyst sword",
                "visiblePhrase": "A decorative sword is mounted on one wall."
            },
        ],
        'extra_items': [
            {
                "name": "oak desk",
                "description": "It's a large oak desk.",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "SET-ME"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "It's way too big to pick up."
                    }
                ],
            },
            {
                "name": "worn chair",
                "description": "It's a well-worn chair.",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "SET-ME"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "You could get it, but where would you put it?"
                    }
                ],
            },
            {
                "name": "bookshelves",
                "description": "They cover every wall from floor to ceiling.",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "SET-ME"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "They can't be moved."
                    }
                ],
            },
            {
                "name": "books",
                "description": "Hundreds of books, ranging from Hungry Hungry Catepillar to See Spot Run",
                "property_dicts": [
                    {
                        "visible": False,
                        "visiblePhrase": "SET-ME"
                    },
                    {
                        "gettable": False,
                        "getPhrase": "Get ALL the books??"
                    }
                ],
            }
        ],
    }

    def room_data(self):
        """ getter """
        return self._room_data
