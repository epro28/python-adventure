class DataItemSign:
    """ Item Data"""
    item_data = {
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
    }


def item_data(self):
    """ getter """
    return self.item_data
