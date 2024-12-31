class DataItemWoodenKey:  # pylint: disable=too-few-public-methods
    """ Item Data"""
    _item_data = {
        "name": "wooden key",
        "description": "It's a wooden key in the shape of a key.",
        "property_dicts": [
            {
                "visible": False,
                "visiblePhrase": "A key lies in the crease of the opened book."
            },
        ],
    }

    def item_data(self):
        """ getter """
        return self._item_data
