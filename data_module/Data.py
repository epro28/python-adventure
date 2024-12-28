class Data:
    """Data"""
    data = {
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
        'items':
        [
            {
                "name": "cat",
                "description": "It's a feline resembling a tabby cat, with gray fur and surly disposition.",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "A cat tries to not make it obvious that it's watching you."
                    },
                    {
                        "gettable": False,
                        "getPhrase": "It's fur says \"pet me\" but its extended claws say otherwise."
                    },
                    {
                        "talkable": True,
                        "dialog": [
                            "\"Don't see your kind around here much.\", snarls the cat.",
                            "\"By 'Your Kind', I mean fascists.\"",
                            "\"A guy came this way a few months ago looking for a dog.\", continued the cat.",
                            "\"Said he had something valuable to give the dog. Something about paying back an old debt.\"",
                            "\"I don't really care. The whole story sounded fascist to me.\", explained the cat.",
                            "\"I... don't think that word means what you think it means.\", you say.",
                            "The cat just stands there looking disinterested in you now. You are curious about this dog and the valuable item though."
                        ]
                    }
                ]
            },
            {
                "name": "rock",
                "description": "It's a gray rock.",
                "property_dicts": []
            },
            {
                "name": "box",
                "description": "It's a box made of stone. I mean wood.",
                "property_dicts": [
                    {
                        "unlocked": False,
                        "otherItemName": "key",
                        "desc": "It's an unlocked stone box. I mean wood box."
                    },
                    {
                        "opened": False,
                        "desc": "It's an opened box made of stone. I mean wood.",
                        "revealedItem": {
                            "name": "scroll",
                            "revealedPhrase": "There was a scroll inside!"
                        }
                    }
                ],
            },
            {
                "name": "dent",
                "description": "It's your fault.",
                "property_dicts": [
                    {
                        "gettable": False,
                        "getPhrase": "Just leave the dent there. You've done enough already."
                    }
                ],
            },
            {
                "name": "broom",
                "description": "A broom (also known as a broomstick) is a cleaning tool consisting of usually stiff fibers (often made of materials such as plastic, hair, or corn husks) attached to, and roughly parallel to, a cylindrical handle, the broomstick. It is thus a variety of brush with a long handle. It is commonly used in combination with a dustpan.",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "Someone has irresponsibly left a broom out in the open. Unexposed, unlocked, and vulnerable."
                    },
                ],
            },
            {
                "name": "scroll",
                "description": "This dusty scroll appears to have been sealed for tens of years.",
                "property_dicts": [
                    {
                        "opened": False,
                        "desc": "It's a dusty scroll with a single word written in it: 'ABRACADABRA'"
                    }
                ],
            },
            {
                "name": "key",
                "description": "A key in the shape of a key.",
                "property_dicts": [],
            },
            {
                "name": "candle",
                "description": "It's a lonely candle waiting for the perfect match.",
                "property_dicts": [
                    {
                        "lit": False,
                        "otherItemName": "match",
                        "desc": "It's a brightly glowing candle that has found its match."
                    }
                ]
            },
            {
                "name": "match",
                "description": "It's a lonely match just waiting to make a spark with someone.",
                "property_dicts": []
            },
            {
                "name": "sign",
                "description": "It says \"DROP *** TREASURE *** HERE\".",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "A wooden sign is planted conspicuously in one corner."
                    },
                    {
                        "gettable": False,
                        "getPhrase": "It's firmly planted in the ground."
                    }
                ]
            },
            {
                "name": "seagull",
                "description": "It's circling above you and doesn't look happy you're here.",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "There's an angry seagull circling above you!"
                    },
                    {
                        "killed": False,
                        "otherItemName": "broom",
                        "killedDescription": "Are you happy now?",
                        "killedPhrase": "You swung the broom and knocked the seagull out of the air!",
                        "killedGetPhrase": "You could get it... but why would you want to?",
                        "killedVisiblePhrase": "There's a dead seagull on the floor."
                    },
                    {
                        "gettable": False,
                        "getPhrase": "You can't reach it."
                    },
                ]
            },
            {
                "name": "amethyst sword",
                "description": "As heavy as it is beautiful, this imposing blade shines with a violet iridescence.",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "A decorative sword is mounted on one wall."
                    },
                    {
                        "treasure_value": 10
                    },
                    {
                        "gettable": True,
                        "getPhrase": "It's bound to its new spot as if by destiny."
                    }
                ],
            },
            {
                "name": "opal dagger",
                "description": "A small but deadly weapon with a smooth, jet-black blade and hilt.",
                "property_dicts": [
                    {
                        "treasure_value": 10
                    },
                    {
                        "gettable": True,
                        "getPhrase": "It's bound to its new spot as if by destiny."
                    }
                ],
            },

        ],  # items
        'inventory_items': [
            "rock",
            "box",
            "key",
            "match",
            "candle",
        ],  # inventory
        'map_rooms': [
            {
                "coordinates": "0,0",
                "room_name": "basic room",
                "item_names": ["seagull", "sign", "cat"],
                "is_treasure_room": "True"
            },
            {
                "coordinates": "1,0",
                "room_name": "trampoline room",
                "item_names": ["amethyst sword"]
            },
            {
                "coordinates": "2,0",
                "room_name": "broom room",
                "item_names": ["broom"]
            },
            {
                "coordinates": "1,1",
                "room_name": "cat room",
                "item_names": ["opal dagger"]
            },
        ],  # map
    }

    # Getters

    def items(self):
        return self.data["items"]

    def rooms(self):
        return self.data["rooms"]

    def mapRooms(self):
        return self.data["map_rooms"]

    def inventoryItemNames(self):
        return self.data["inventory_items"]
