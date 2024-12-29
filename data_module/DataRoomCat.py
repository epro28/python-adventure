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
        ]
    }

    def room_data(self):
        """ getter """
        return self._room_data
