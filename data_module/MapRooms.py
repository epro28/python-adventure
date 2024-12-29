""" MapRooms.py """


class MapRooms:  # pylint: disable=too-few-public-methods
    """ Map Rooms """
    map_rooms = [
        {
            "coordinates": "0,0",
            "room_name": "basic room",
            "item_names": ["seagull", "sign", "box", "match"],
            "is_treasure_room": "True"
        },
        {
            "coordinates": "1,0",
            "room_name": "trampoline room",
            "item_names": ["amethyst sword", "candle", "key"]
        },
        {
            "coordinates": "2,0",
            "room_name": "broom room",
            "item_names": ["broom"]
        },
        {
            "coordinates": "1,1",
            "room_name": "cat room",
            "item_names": ["opal dagger", "cat"]
        },
    ]  # map


def map_rooms(self):
    """ getter """
    return self.map_rooms
