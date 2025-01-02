""" MapRooms.py """


class MapRooms:  # pylint: disable=too-few-public-methods
    """ Map Rooms """
    _map_rooms = [
        ##  ROW 0  ################################
        {
            "coordinates": "0,0",
            "room_data": {
                "name": "outskirts00",
                "description": "You are in clearing, bounded by a dense forest \
                    to the north and west. The clearing extends to the east and\
                          south as far as the eye can see.",
                "symbol": "🟩",
                'doors':
                [
                    {
                        "direction": "e",
                        "description": "The clearing continues to the east as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "w",
                        "description": "There's a dense forest to the west.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    },
                    {
                        "direction": "s",
                        "description": "The clearing continues to the south as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "n",
                        "description": "There's a dense forest to the north.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    }
                ],
            }
        },
        {
            "coordinates": "1,0",
            "room_data": {
                "name": "outskirts10",
                "description": "You are in clearing, bounded by a dense forest \
                    to the north. The clearing extends to the east as far as \
                        you can see. You can see a forest line in the distance \
                            to the west. There is a gray stone wall a few steps\
                                  to the south.",
                "symbol": "🟩",
                'doors':
                [
                    {
                        "direction": "e",
                        "description": "The clearing continues to the east as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "w",
                        "description": "You can see a forest line in the distance to the west.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "s",
                        "description": "There is a gray stone wall a few steps to the south.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "n",
                        "description": "There's a dense forest to the north.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    }
                ],
            }
        },
        {
            "coordinates": "2,0",
            "room_data": {
                "name": "outskirts20",
                "description": "You are in clearing, bounded by a dense forest \
                    to the north. The clearing extends to the east as far as \
                        you can see. You can see a forest line in the far \
                            distance to the west. You're on the north edge of a\
                                  gray stone building.",
                "symbol": "🟩",
                'doors':
                [
                    {
                        "direction": "e",
                        "description": "The clearing continues to the east as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "w",
                        "description": "You can see a forest line far in the far distance to the west.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "s",
                        "description": "You're on the north edge of a gray stone building.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You don't see any way over, around, or through the stone wall."
                            }
                        ]
                    },
                    {
                        "direction": "n",
                        "description": "There's a dense forest to the north.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    }
                ],
            }
        },
        {
            "coordinates": "3,0",
            "room_data": {
                "name": "outskirts30",
                "description": "You are in clearing, bounded by a dense forest \
                    to the north. The clearing extends to the east and west as \
                        far as you can see. There's a window just above \
                            eye-level in the gray stone wall to the south.",
                "symbol": "🟩",
                'doors':
                [
                    {
                        "direction": "e",
                        "description": "The clearing continues to the east as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "w",
                        "description": "The clearing continues to the west as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "s",
                        "description": "If you stand on your toes you can just \
                            make out the interior of the room through the \
                                window. TODO: add content",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "Passage through the window is blocked by iron bars."
                            }
                        ]
                    },
                    {
                        "direction": "n",
                        "description": "There's a dense forest to the north.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    }
                ],
            }
        },
        {
            "coordinates": "4,0",
            "room_data": {
                "name": "outskirts40",
                "description": "You are in clearing, bounded by a dense forest \
                    to the north. The clearing extends to the east and west as \
                        far as you can see. You're on the north edge of a gray \
                            stone building.",
                "symbol": "🟩",
                'doors':
                [
                    {
                        "direction": "e",
                        "description": "The clearing continues to the east as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "w",
                        "description": "The clearing continues to the west as far as you can see.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "s",
                        "description": "You're on the north edge of a building made of gray stone.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You don't see any way over, around, or through the stone wall."
                            }
                        ]
                    },
                    {
                        "direction": "n",
                        "description": "There's a dense forest to the north.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    }
                ],
            }
        },
        {
            "coordinates": "5,0",
            "room_name": "study"
        },
        {
            "coordinates": "6,0",
            "room_name": "study"
        },
        ##  ROW 1  ################################
        {
            "coordinates": "0,1",
            "room_data": {
                "name": "outskirts01",
                "description": "You step out of the forest and into a clearing.\
                      The dirt path that lead you here turns to the south. \
                        Straight ahead to the east you make out a gray building.",
                "symbol": "🟩",
                'doors':
                [
                    {
                        "direction": "e",
                        "description": "Straight ahead to the east you make out a gray building.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "w",
                        "description": "The forest and the dirt path that lead you here lies to the west.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    },
                    {
                        "direction": "s",
                        "description": "The dirt path that lead you here turns to the south.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "n",
                        "description": "You can see a forest line in the distance to the west.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    }
                ],
            }
        },
        {
            "coordinates": "1,1",
            "room_name": "study"
        },
        {
            "coordinates": "2,1",
            "room_name": "study"
        },
        {
            "coordinates": "3,1",
            "room_name": "study"
        },
        {
            "coordinates": "4,1",
            "room_name": "study"
        },
        {
            "coordinates": "5,1",
            "room_name": "study"
        },
        {
            "coordinates": "6,1",
            "room_name": "study"
        },
        ##  ROW 2  ################################
        {
            "coordinates": "0,2",
            "room_data": {
                "name": "outskirts02",
                "description": "A dirt path continues to the north and south. \
                    You are outside a stone building to the east. To your west \
                        is a dense forest.",
                "symbol": "🟩",
                'doors':
                [
                    {
                        "direction": "e",
                        "description": "To the east is the outer wall of a gray stone building.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You don't see any way over, around, or through the stone wall."
                            }
                        ]
                    },
                    {
                        "direction": "w",
                        "description": "There's a dense forest to the west.",
                        "property_dicts": [
                            {
                                "passable": False,
                                "passPhrase": "You have no desire to re-enter the forest at this point."
                            }
                        ]
                    },
                    {
                        "direction": "s",
                        "description": "The dirt path continues to the south.",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    },
                    {
                        "direction": "n",
                        "description": "The dirt path continues to the north",
                        "property_dicts": [
                            {
                                "passable": True,
                                "passPhrase": ""
                            }
                        ]
                    }
                ],
            }
        },
        {
            "coordinates": "1,2",
            "room_name": "study"
        },
        {
            "coordinates": "2,2",
            "room_name": "study"
        },
        {
            "coordinates": "3,2",
            "room_name": "study"
        },
        {
            "coordinates": "4,2",
            "room_name": "study"
        },
        {
            "coordinates": "5,2",
            "room_name": "study"
        },
        {
            "coordinates": "6,2",
            "room_name": "study"
        },
        ##  ROW 3  ################################
        {
            "coordinates": "0,3",
            "room_name": "front door"
        },
        {
            "coordinates": "1,3",
            "room_name": "basic room"
        },
        {
            "coordinates": "2,3",
            "room_name": "trampoline room"
        },
        {
            "coordinates": "3,3",
            "room_name": "study"
        },
        {
            "coordinates": "4,3",
            "room_name": "study"
        },
        {
            "coordinates": "5,3",
            "room_name": "study"
        },
        {
            "coordinates": "6,3",
            "room_name": "study"
        },
        ##  ROW 4  ################################
        {
            "coordinates": "0,4",
            "room_name": "study"
        },
        {
            "coordinates": "1,4",
            "room_name": "study"
        },
        {
            "coordinates": "2,4",
            "room_name": "study"
        },
        {
            "coordinates": "3,4",
            "room_name": "study"
        },
        {
            "coordinates": "4,4",
            "room_name": "study"
        },
        {
            "coordinates": "5,4",
            "room_name": "study"
        },
        {
            "coordinates": "6,4",
            "room_name": "study"
        },
        ##  ROW 5  ################################
        {
            "coordinates": "0,5",
            "room_name": "study"
        },
        {
            "coordinates": "1,5",
            "room_name": "study"
        },
        {
            "coordinates": "2,5",
            "room_name": "study"
        },
        {
            "coordinates": "3,5",
            "room_name": "study"
        },
        {
            "coordinates": "4,5",
            "room_name": "study"
        },
        {
            "coordinates": "5,5",
            "room_name": "study"
        },
        {
            "coordinates": "6,5",
            "room_name": "study"
        },
        ##  ROW 6  ################################
        {
            "coordinates": "0,6",
            "room_name": "study"
        },
        {
            "coordinates": "1,6",
            "room_name": "study"
        },
        {
            "coordinates": "2,6",
            "room_name": "study"
        },
        {
            "coordinates": "3,6",
            "room_name": "study"
        },
        {
            "coordinates": "4,6",
            "room_name": "study"
        },
        {
            "coordinates": "5,6",
            "room_name": "study"
        },
        {
            "coordinates": "6,6",
            "room_name": "study"
        },
    ]  # map

    def map_rooms(self):
        """ getter """
        return self._map_rooms
