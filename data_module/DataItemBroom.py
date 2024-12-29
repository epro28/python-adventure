class DataItemBroom:  # pylint: disable=too-few-public-methods
    """ Item Data"""

    _item_data = {
        "name": "broom",
        "description": "A broom (also known as a broomstick) is a cleaning tool consisting of usually stiff fibers (often made of materials such as plastic, hair, or corn husks) attached to, and roughly parallel to, a cylindrical handle, the broomstick. It is thus a variety of brush with a long handle. It is commonly used in combination with a dustpan.",
        "property_dicts": [
            {
                "visible": True,
                "visiblePhrase": "Someone has irresponsibly left a broom out in the open. Unexposed, unlocked, and vulnerable."
            },
        ],
    }

    def item_data(self):
        """ getter """
        return self._item_data
