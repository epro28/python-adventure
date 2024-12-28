class DataItemBox:
    """ Item Data"""
    item_data = {
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
    }


def item_data(self):
    """ getter """
    return self.item_data
