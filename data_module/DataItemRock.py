class DataItemRock:  # pylint: disable=too-few-public-methods
    """ Item Data"""
    _item_data = {
        "name": "rock",
        "description": "It's a gray rock.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "SET ME"
            },
        ]
    }

    def item_data(self):
        """ getter """
        return self._item_data
