class DataItemScroll:
    """ Item Data"""
    item_data = {
        "name": "scroll",
        "description": "This dusty scroll appears to have been sealed for tens of years.",
        "property_dicts": [
            {
                "opened": False,
                "desc": "It's a dusty scroll with a single word written in it: 'ABRACADABRA'"
            }
        ],
    }


def item_data(self):
    """ getter """
    return self.item_data
