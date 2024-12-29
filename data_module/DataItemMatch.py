class DataItemMatch:  # pylint: disable=too-few-public-methods
    """ Item Data"""
    _item_data = {
        "name": "match",
        "description": "It's a lonely match just waiting to make a spark with someone.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "A single match lies on the table."
            },
        ]
    }

    def item_data(self):
        """ getter """
        return self._item_data
