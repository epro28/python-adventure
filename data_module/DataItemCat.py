class DataItemCat:  # pylint: disable=too-few-public-methods
    """ Item Data"""
    _item_data = {
        "name": "cat",
        "description": "It's a feline resembling a tabby cat, with gray fur and surly disposition.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "SET-ME"
            },
            {
                "gettable": False,
                "getPhrase": "It's fur says \"pet me\" but its extended claws say otherwise."
            },
            {
                "talkable": True,
                "dialog": [
                    "\"Don't see your kind around here much.\", snarls the cat.",
                    "\"By 'Your Kind', I mean fascists.\"",
                    "\"A guy came this way a few months ago looking for a dog.\", continued the cat.",
                    "\"Said he had something valuable to give the dog. Something about paying back an old debt.\"",
                    "\"I don't really care. The whole story sounded fascist to me.\", explained the cat.",
                    "\"I... don't think that word means what you think it means.\", you say.",
                    "The cat just stands there looking disinterested in you now. You are curious about this dog and the valuable item though."
                ]
            }
        ]
    }

    def item_data(self):
        """ getter """
        return self._item_data
