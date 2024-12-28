class DataItemDent:
    """ Item Data"""
    item_data = {
        "name": "dent",
        "description": "It's your fault.",
        "property_dicts": [
            {
                "gettable": False,
                "getPhrase": "Just leave the dent there. You've done enough already."
            }
        ],
    }


def item_data(self):
    """ getter """
    return self.item_data
