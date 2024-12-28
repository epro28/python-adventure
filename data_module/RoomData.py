class RoomData:
    """ Room Data"""
    room_data = {
        'rooms':
        [
            {
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
            },
            {
                "name": "basic room",
                "description": "You are in the most basic room imaginable. Absolutely nothing memorable about this room.",
                'doors':
                [
                    {
                        "direction": "e",
                        'description': "Through an extremely basic opening to the east you feel a basic breeze.",
                    }
                ],
            },
            {
                "name": "broom room",
                "description": "This is, apparently, a broom room. Wall to wall with brooms locked behind glass cabinet doors.",
                'doors':
                [
                    {
                        "direction": "w",
                        'description': "You can sense pure bounciness to the west.",
                    },
                ]
            },
            {
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
            },
        ],  # rooms
    }

    def rooms(self):
        """ getter """
        return self.room_data["rooms"]
