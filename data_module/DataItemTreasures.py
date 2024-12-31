class DataItemTreasures:
    """ Treasures Data"""  # pylint: disable=too-few-public-methods
    _item_data = {
        'items':
        [
            {
                "name": "opal dagger",
                "description": "A small but deadly weapon with a smooth, jet-black blade and hilt.",
                "property_dicts": [
                    {
                        "visible": True,
                        "visiblePhrase": "On the table is a dagger so dark it appears to absorb the light in its immediate vicinity."
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
        ],  # items
    }

    def items(self):
        """ getter """
        return self._item_data["items"]
