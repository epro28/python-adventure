""" DataManager.py """

from Room import Room
from Item import Item
from data_module.DataItemCat import DataItemCat
from data_module.DataItemRock import DataItemRock
from data_module.DataItemBox import DataItemBox
from data_module.DataItemDent import DataItemDent
from data_module.DataItemBroom import DataItemBroom
from data_module.DataItemScroll import DataItemScroll
from data_module.DataItemKey import DataItemKey
from data_module.DataItemCandle import DataItemCandle
from data_module.DataItemMatch import DataItemMatch
from data_module.DataItemSign import DataItemSign
from data_module.DataItemSeagull import DataItemSeagull
from data_module.DataItemTreasures import DataItemTreasures
from data_module.DataRoomTrampoline import DataRoomTrampoline
from data_module.DataRoomBasic import DataRoomBasic
from data_module.DataRoomBroom import DataRoomBroom
from data_module.DataRoomCat import DataRoomCat
from data_module.Inventory import Inventory
from data_module.MapRooms import MapRooms


class DataManager:
    """ DataManager """

    _rooms = []
    _items = []
    _map_rooms = []
    _inventory_items = []

    def __init__(self):

        # Get items from the data
        data_items = [
            DataItemCat().item_data(),
            DataItemRock().item_data(),
            DataItemBox().item_data(),
            DataItemDent().item_data(),
            DataItemBroom().item_data(),
            DataItemScroll().item_data(),
            DataItemKey().item_data(),
            DataItemCandle().item_data(),
            DataItemMatch().item_data(),
            DataItemSign().item_data(),
            DataItemSeagull().item_data()
        ]
        for treasure in DataItemTreasures().items():
            data_items.append(treasure)
        # Create items from the data
        for data_item in data_items:
            item = Item(data_item["name"])
            item.set_description(data_item["description"])
            item.setPropertyDicts(data_item["property_dicts"])
            self._items.append(item)

        # Create Rooms from data
        data_rooms = [
            DataRoomTrampoline().room_data(),
            DataRoomBasic().room_data(),
            DataRoomBroom().room_data(),
            DataRoomCat().room_data()
        ]
        for data_room in data_rooms:
            room = Room(data_room["name"])
            room.set_description(data_room["description"])
            room.setDoors(data_room["doors"])
            self._rooms.append(room)

        self._inventory_items = Inventory().inventory
        self._map_rooms = MapRooms().map_rooms

    def rooms(self):
        """ rooms """
        return self._rooms

    def items(self):
        """ items """
        return self._items

    def inventory_items(self):
        """ getter """
        return self._inventory_items

    def map_rooms(self):
        """ getter """
        return self._map_rooms

    def item(self, name):
        """ getter """
        for item in self._items:
            if item.name() == name:
                return item
        print("!!! Couldn't find item in data (" + name + ")")
        return None

    def room(self, name):
        for room in self._rooms:
            if room.name() == name:
                return room
        print("!!! Couldn't find room in data")
        return None
