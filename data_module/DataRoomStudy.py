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
        'items': [],
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
        ]
    }

    def room_data(self):
        """ getter """
        return self._room_data
