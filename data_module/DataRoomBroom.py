class DataRoomBroom:
    """ Room Data"""
    room_data = {
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
    return self.room_data
