class DataItemSeagull:
    """ Item Data"""
    _item_data = {
        "name": "seagull",
        "description": "It's circling above you and doesn't look happy you're here.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "There's an angry seagull circling above you!"
            },
            {
                "killed": False,
                "otherItemName": "broom",
                "killedDescription": "Are you happy now?",
                "killedPhrase": "You swung the broom and knocked the seagull out of the air!",
                "killedGetPhrase": "You could get it... but why would you want to?",
                "killedVisiblePhrase": "There's a dead seagull on the floor."
            },
            {
                "gettable": False,
                "getPhrase": "You can't reach it."
            },
        ]
    }

    def item_data(self):
        """ getter """
        return self._item_data
