""" DataRoomCat.py """


class DataRoomCat:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "cat room",
        "description": "A room filled with scratching posts and milk saucers.",
        'doors':
        [
            {
                "direction": "n",
                'description': "Pure bounciness to the north.",
                'locked': False
            },
        ],
        'items': [],
        'room_items':
        [
            {
                "name": "cat",
                "visiblePhrase": "A cat tries to not make it obvious that it's watching you."
            },
        ]
    }

    def room_data(self):
        """ getter """
        return self._room_data
