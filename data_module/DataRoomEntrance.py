""" DataRoomEntrance.py """


class DataRoomEntrance:  # pylint: disable=too-few-public-methods
    """ Room Data"""
    _room_data = {
        "template": "castle",
        "name": "entrance",
        "description": "You are in the entryway to a castle. \
            Despite its age the marble floors somehow retain a foggy luster. \
                Hallways lead to the north and east. \
                    There is a red door to the south.",
        'doors':
        [
            {
                "direction": "e",
                "description": "A hallway leads to the east.",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "w",
                "description": "Sunlight radiates through the castle's entryway.",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "s",
                "description": "Undoubtedly stunning in a previous life, \
                    this ruby-red door shows more than a few years of age.",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            },
            {
                "direction": "n",
                "description": "A hallway leads to the north.",
                "property_dicts": [
                    {
                        "passable": True,
                        "passPhrase": ""
                    }
                ]
            }
        ],
        'room_items':
        [],
        'extra_items':
        [],
    }

    def room_data(self):
        """ getter """
        return self._room_data
