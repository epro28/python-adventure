class DataRoomBroom:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "name": "broom room",
        "description": "This is, apparently, a broom room. Wall to wall with brooms locked behind glass cabinet doors.",
        'doors':
        [
            {
                "direction": "w",
                'description': "You can sense pure bounciness to the west.",
            },
        ]
    }

    def room_data(self):
        """ getter """
        return self._room_data
