""" DataRoomMisc.py """


class DataRoomMisc:  # pylint: disable=too-few-public-methods
    """ Misc Data Rooms """
    _misc_rooms = [
        ##  ROW 0  ################################
        {
            "template": "outskirts",
            "name": "outskirts00",
            "description": "You're at the northwest corner of a stone buiding. \
                There is a dense forest to the north and west.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "There is a dense forest to the west.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A dirt path emerging from the forest begins and extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "There is a dense forest to the north.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts10",
            "description": "You're walking along the north edge of a stone building. \
                To the north is a dense forest.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "There is a dense forest to the north.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts20",
            "description": "You're walking along the north edge of a stone building. \
                To the north is a dense forest.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "There is a dense forest to the north.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts30",
            "description": "You're walking along the north edge of a stone building. \
                To the north is a dense forest. \
                    To the east you hear the sound of rushing water.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "There is a dense forest to the north.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts40",
            "description": "You're at the northeast corner of a stone buiding. \
                A deep ravine with a raging river at the bottom opens to the east.\
                    There is a dense forest to the north.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "Your stomach churns as you look down into the ravine.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "There is only one way to go in this direction, \
                                and that is to a watery doom at the bottom of the ravine."
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A narrow, dangerous path along the ravine extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "There is a dense forest to the north.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
            ],
        },
        ##  ROW 1  ################################
        {
            "template": "outskirts",
            "name": "outskirts01",
            "description": "You're standing at a trailhead that leads into a dense forest to the west. \
                A dirt path runs to the south. \
                A stone building looms over you to the east.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "There is a dense forest to the west.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A dirt path extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "A grass path extends to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts41",
            "description": "Outskirts41",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "Your stomach churns as you look down into the ravine.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "There is only one way to go in this direction, \
                                and that is to a watery doom at the bottom of the ravine."
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A narrow, dangerous path along the ravine extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "A narrow, dangerous path along the ravine extends to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
        ##  ROW 2  ################################
        {
            "template": "outskirts",
            "name": "outskirts02",
            "description": "You're standing outside the door to the stone building. A dense forest is to the west.\
                A dirt path runs to the north.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "You're standing outside the door to the stone building.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "There is a dense forest to the west.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A grass path extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "A dirt path extends to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts42",
            "description": "Outskirts42",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "Your stomach churns as you look down into the ravine.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "There is only one way to go in this direction, \
                                and that is to a watery doom at the bottom of the ravine."
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A narrow, dangerous path along the ravine extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "A narrow, dangerous path along the ravine extends to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
        ##  ROW 3  ################################
        {
            "template": "outskirts",
            "name": "outskirts03",
            "description": "Outskirts03",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "There is a dense forest to the west.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A grass path extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "The beginning of a dirt path is to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts43",
            "description": "Outskirts43",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "Your stomach churns as you look down into the ravine.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "There is only one way to go in this direction, \
                                and that is to a watery doom at the bottom of the ravine."
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "A narrow, dangerous path along the ravine extends to the south.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "A narrow, dangerous path along the ravine extends to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
        ##  ROW 4  ################################
        {
            "template": "outskirts",
            "name": "outskirts04",
            "description": "You're at the southwest corner of a stone buiding. There is a dense forest to the south and west.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "There is a dense forest to the west.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "There is a dense forest to the south.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "A grass path extends to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts14",
            "description": "You're walking along the south edge of a stone building. \
                To the south is a dense forest.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "There is a dense forest to the south.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                }
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts24",
            "description": "You're walking along the south edge of a stone building. \
                To the south is a dense forest.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "There is a dense forest to the south.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                }
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts34",
            "description": "You're walking along the south edge of a stone building. \
                To the south is a dense forest. \
                    To the east you hear the sound of rushing water.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "A grass path extends to the east.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "There is a dense forest to the south.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "You see only the solid, towering wall of the stone building.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You see no way over, around, or through the stone wall."
                        }
                    ]
                }
            ],
        },
        {
            "template": "outskirts",
            "name": "outskirts44",
            "description": "You're at the southeast corner of a stone buiding. \
                A deep ravine with a raging river at the bottom opens to the east.\
                    There is a dense forest to the south.",
            'doors':
            [
                {
                    "direction": "e",
                    "description": "Your stomach churns as you look down into the ravine.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "There is only one way to go in this direction, \
                                and that is to a watery doom at the bottom of the ravine."
                        }
                    ]
                },
                {
                    "direction": "w",
                    "description": "A grass path extends to the west.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                },
                {
                    "direction": "s",
                    "description": "There is a dense forest to the south.",
                    "property_dicts": [
                        {
                            "passable": False,
                            "passPhrase": "You have no desire to return to the forest at this time."
                        }
                    ]
                },
                {
                    "direction": "n",
                    "description": "A narrow, dangerous path along the ravine extends to the north.",
                    "property_dicts": [
                        {
                            "passable": True,
                            "passPhrase": ""
                        }
                    ]
                }
            ],
        },
    ]  # map

    def misc_rooms(self):
        """ getter """
        return self._misc_rooms
