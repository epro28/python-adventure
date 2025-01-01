""" DataRoomTrampoline.py """


class DataRoomTrampoline:  # pylint: disable=too-few-public-methods
    """ Item Data"""
    _room_data = {
        "name": "trampoline room",
        'description': "This is the bounciest room imaginable, due to the floor being made entirely of trampolines.",
        'doors':
        [
            {
                "direction": "e",
                'description': "Bouncing and peering over the wall to the east you see a passage.",
            },
            {
                "direction": "w",
                'description': "You sense pure mediocrity to the west.",
            },
            {
                "direction": "s",
                'description': "A short hallway to the south leads to a room with a small opening, just big enough to crawl through.",
            }
        ],
        'extra_items': [],
        'room_items': []
    }

    def room_data(self):
        """ getter """
        return self._room_data
