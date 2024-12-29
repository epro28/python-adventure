class DataItemRock:
    """ Item Data"""
    _item_data = {
        "name": "rock",
        "description": "It's a gray rock.",
        "property_dicts": []
    }

    def item_data(self):
        """ getter """
        return self._item_data
