class DataRoomBasic:
    """ Room Data"""
    room_data = {
        "name": "basic room",
        "description": "You are in the most basic room imaginable. Absolutely nothing memorable about this room.",
        'doors':
        [
            {
                "direction": "e",
                'description': "Through an extremely basic opening to the east you feel a basic breeze.",
            }
        ],
    }


def room_data(self):
    """ getter """
    return self.room_data
