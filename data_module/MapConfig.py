""" MapConfig.py """


class MapConfig:  # pylint: disable=too-few-public-methods
    """ Map Config """
    _map_config = [
        ##  ROW 0  ################################
        {
            "coordinates": "0,0",
            "name": "outskirts00",
        },
        {
            "coordinates": "1,0",
            "name": "outskirts10",
        },
        {
            "coordinates": "2,0",
            "name": "outskirts20",
        },
        {
            "coordinates": "3,0",
            "name": "outskirts30",
        },
        {
            "coordinates": "4,0",
            "name": "outskirts40",
        },
        ##  ROW 1  ################################
        {
            "coordinates": "0,1",
            "name": "outskirts01",
        },
        {
            "coordinates": "1,1",
            "name": "blue room",
        },
        {
            "coordinates": "2,1",
            "name": "castle21"
        },
        {
            "coordinates": "3,1",
            "name": "castle31"
        },
        {
            "coordinates": "4,1",
            "name": "outskirts41",
        },
        ##  ROW 2  ################################
        {
            "coordinates": "0,2",
            "name": "outskirts02",
        },
        {
            "coordinates": "1,2",
            "name": "entrance"
        },
        {
            "coordinates": "2,2",
            "name": "basic room"
        },
        {
            "coordinates": "3,2",
            "name": "castle32"
        },
        {
            "coordinates": "4,2",
            "name": "outskirts42",
        },
        ##  ROW 3  ################################
        {
            "coordinates": "0,3",
            "name": "outskirts03",
        },
        {
            "coordinates": "1,3",
            "name": "castle13"
        },
        {
            "coordinates": "2,3",
            "name": "castle23"
        },
        {
            "coordinates": "3,3",
            "name": "castle33"
        },
        {
            "coordinates": "4,3",
            "name": "outskirts43",
        },
        ##  ROW 4  ################################
        {
            "coordinates": "0,4",
            "name": "outskirts04",
        },
        {
            "coordinates": "1,4",
            "name": "outskirts14",
        },
        {
            "coordinates": "2,4",
            "name": "outskirts24",
        },
        {
            "coordinates": "3,4",
            "name": "outskirts34",
        },
        {
            "coordinates": "4,4",
            "name": "outskirts44",
        },
    ]  # map

    def map_config(self):
        """ getter """
        return self._map_config
