class DataRoomTrampoline:
    """ Item Data"""
    room_data = {
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
        ]
    }


def room_data(self):
    """ getter """
    return self.room_data
