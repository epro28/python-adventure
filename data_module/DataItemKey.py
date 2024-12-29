class DataItemKey:  # pylint: disable=too-few-public-methods
    """ Item Data"""
    _item_data = {
        "name": "key",
        "description": "A key in the shape of a key.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "A key lies in the crease of an opened book."
            },
        ],
    }

    def item_data(self):
        """ getter """
        return self._item_data
