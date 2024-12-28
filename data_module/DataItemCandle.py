class DataItemCandle:
    """ Item Data"""
    item_data = {
        "name": "candle",
        "description": "It's a lonely candle waiting for the perfect match.",
        "property_dicts": [
            {
                "lit": False,
                "otherItemName": "match",
                "desc": "It's a brightly glowing candle that has found its match."
            }
        ]
    }


def item_data(self):
    """ getter """
    return self.item_data
