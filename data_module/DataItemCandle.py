""" DataItemCandle.py """


class DataItemCandle:  # pylint: disable=too-few-public-methods
    """ Item Data"""
    _item_data = {
        "name": "candle",
        "description": "It's a lonely candle waiting for the perfect match.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "SET-ME"
            },
            {
                "lit": False,
                "otherItemName": "match",
                "desc": "It's a brightly glowing candle that has found its match."
            }
        ]
    }

    def item_data(self):
        """ getter """
        return self._item_data
