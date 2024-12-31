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
            {
                "direction": "e",
                'description': "A hallway extends to the east, ending at a large half-open oak door.",
            },
        ],
        'items': [],
        'room_items':
        [
            {
                "name": "broom",
                "visiblePhrase": "Someone has irresponsibly left a broom out in the open. Unexposed, unlocked, and vulnerable."
            },
        ]
    }

    def room_data(self):
        """ getter """
        return self._room_data
