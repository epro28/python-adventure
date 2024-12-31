class DataItemWoodenBox:
    """ Item Data"""
    _item_data = {
        "name": "wooden box",
        "description": "It's a box made of stone. I mean wood.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "A wooden box lies on its side in the middle of the floor."
            },
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
        return self._item_data
