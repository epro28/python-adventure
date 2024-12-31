class DataItemRedBook:
    """ Item Data"""
    _item_data = {
        "name": "red book",
        "description": "It's a book bound in brown leather, with a stripe of red \
            along the binding and cover.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "SET-ME"
            },
            {
                "opened": False,
                "desc": "It's a book bound in brown leather, with a stripe of red\
                        along the binding and cover.",
                "revealedItem": {
                    "name": "wooden key",
                    "revealedPhrase": "You open the book along the most prominent\
                            crease and find a key marking the page."
                }
            }
        ],
    }

    def item_data(self):
        """ getter """
        return self._item_data
