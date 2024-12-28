class DataItemTreasures:
    """ Treasures Data"""
    item_data = {
        'items':
        [
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
    }

    # Getters

    def items(self):
        """ getter """
        return self.item_data["items"]
