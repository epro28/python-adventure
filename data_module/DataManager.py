""" DataManager.py """

import copy
from Room import Room
from Item import Item
from helper_functions import tidy
from data_module.PlayerConfig import PlayerConfig
from data_module.DataRoomMisc import DataRoomMisc
from data_module.DataRoomCastleTemplate import DataRoomCastleTemplate
from data_module.DataRoomOutskirtsTemplate import DataRoomOutskirtsTemplate
from data_module.DataRoomStudy import DataRoomStudy
from data_module.DataRoomTrampoline import DataRoomTrampoline
from data_module.DataRoomBasic import DataRoomBasic
from data_module.DataRoomBroom import DataRoomBroom
from data_module.DataRoomCat import DataRoomCat
from data_module.DataRoomFrontDoor import DataRoomFrontDoor
from data_module.DataItemTreasures import DataItemTreasures
from data_module.DataItemWoodenKey import DataItemWoodenKey
from data_module.DataItemWoodenBox import DataItemWoodenBox
from data_module.DataItemRedBook import DataItemRedBook
# from data_module.DataItemRock import DataItemRock
# from data_module.DataItemDent import DataItemDent
# from data_module.DataItemScroll import DataItemScroll
# from data_module.DataItemKey import DataItemKey
from data_module.DataItemCat import DataItemCat
from data_module.DataItemCandle import DataItemCandle
from data_module.DataItemBroom import DataItemBroom
# from data_module.DataItemMatch import DataItemMatch
# from data_module.DataItemSign import DataItemSign
# from data_module.DataItemSeagull import DataItemSeagull


class DataManager:
    """ DataManager """

    _rooms = []
    _room_templates = []
    _items = []
    # _map_rooms = []
    _inventory_items = []
    _player_position = []

    def __init__(self):

        self._inventory_items = PlayerConfig().inventory_items()
        pos_x, pos_y = PlayerConfig().position()
        self._player_position.append(pos_x)
        self._player_position.append(pos_y)

        # Get items from the data
        data_items = [
            DataItemRedBook().item_data(),
            DataItemWoodenBox().item_data(),
            DataItemWoodenKey().item_data(),
            #    DataItemRock().item_data(),
            #    DataItemDent().item_data(),
            #    DataItemScroll().item_data(),
            DataItemCat().item_data(),
            DataItemCandle().item_data(),
            DataItemBroom().item_data(),
            #    DataItemMatch().item_data(),
            #    DataItemSign().item_data(),
            #    DataItemSeagull().item_data(),
        ]
        for treasure in DataItemTreasures().items():
            data_items.append(treasure)
        # Create items from the data
        for data_item in data_items:
            item = Item(data_item["name"])
            item.set_description(data_item["description"])
            item.setPropertyDicts(data_item["property_dicts"])
            self._items.append(item)

        # ==============================================================

        # load in template data
        # construct room templates
        # load in pre-built room data
        # construct rooms, starting with template, and adding from there
        # load in map data,
        #   1. constructing rooms using the data
        #   2. constructing rooms using simply references to pre-build rooms
        #   3. in both cases, add rooms to map using coordindates

        data_room_templates = self.load_in_template_data()

        self._room_templates = self.make_rooms(
            data_room_templates, data_room_templates)

        data_rooms = self.load_in_room_data()

        self._rooms = self.make_rooms(data_rooms, data_room_templates)

        misc_rooms = self.make_rooms(
            DataRoomMisc().misc_rooms(), data_room_templates)

        for misc_room in misc_rooms:
            print(misc_room.name())
        # ==============================================================

        # loading room data dicts from any room data dict embedded in MapRooms.py
        # for map_room in self._map_rooms:
        #    if "room_data" in map_room:
        #        data_rooms.append(map_room["room_data"])

        # at this point we have a room list

    # def make_room_templates(self, data_room_templates):
    #    room_templates = []
    #    for data_room_template in data_room_templates:
    #        room_template = self.make_room_from_dict(data_room_template)
    #        room_templates.append(room_template)
    #    return room_templates

    def make_rooms(self, data_rooms, data_room_templates):
        rooms = []
        for data_room in data_rooms:
            # if there's a template, do a copy of an existing room template;
            # otherwise create the room uniquely
            if "template" in data_rooms:
                room = copy.deepcopy(self.room_template(
                    data_room_templates["template"]))
            else:
                room = Room(data_room["name"])
            self.set_name_from_data(data_room, room)
            self.set_description_from_data(data_room, room)
            self.set_symbol_from_data(data_room, room)
            self.set_doors_from_data(data_room, room)
            self.set_room_items_from_data(data_room, room)
            self.set_extra_items_from_data(data_room, room)
            rooms.append(room)
        return rooms

    def load_in_template_data(self):
        data_room_templates = [
            DataRoomOutskirtsTemplate().room_data(),
            DataRoomCastleTemplate().room_data(),
        ]
        return data_room_templates

    def load_in_room_data(self):
        # load in the room data
        data_rooms = [
            DataRoomTrampoline().room_data(),
            DataRoomBasic().room_data(),
            DataRoomBroom().room_data(),
            DataRoomCat().room_data(),
            DataRoomStudy().room_data(),
            DataRoomFrontDoor().room_data(),
        ]
        return data_rooms

    # def make_rooms(self, data_rooms, room_templates):
    #    for data_room in data_rooms:

    def player_position(self):
        """ getter """
        return self._player_position

    def rooms(self):
        """ getter """
        return self._rooms

    def items(self):
        """ items """
        return self._items

    def inventory_items(self):
        """ getter """
        return self._inventory_items

    # def map_rooms(self):
    #    """ getter """
    #    return self._map_rooms

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
        print("!!! Couldn't find room in data (" + name + ")")
        return None

    def room_template(self, name):
        for room_template in self._room_templates:
            if room_template.name() == name:
                return room_template
        print("!!! Couldn't find room in data (" + name + ")")
        return None

    def set_name_from_data(self, dict, room):
        prop = "room_name"
        if prop in dict:
            room.set_name(dict[prop])

    def set_description_from_data(self, dict, room):
        prop = "description"
        if prop in dict:
            room.set_description(dict[prop])

    def set_doors_from_data(self, dict, room):
        prop = "doors"
        if prop in dict:
            room.set_doors(dict[prop])

    def set_symbol_from_data(self, dict, room):
        prop = "symbol"
        if prop in dict:
            room.set_symbol(dict[prop])

    def set_room_items_from_data(self, dict, room):
        prop = "room_items"
        if prop in dict:
            data_room_items = dict[prop]
            for data_room_item in data_room_items:
                name = data_room_item["name"]
                visiblePhrase = data_room_item["visiblePhrase"]
                item = self.item(name)
                item.set_property("visiblePhrase", visiblePhrase)
                room.add_item(item)

    def set_extra_items_from_data(self, dict, room):
        prop = "extra_items"
        if prop in dict:
            data_extra_items = dict[prop]
            for data_extra_item in data_extra_items:
                name = data_extra_item["name"]
                # TODO: fully import an item
                # visiblePhrase = data_extra_item["visiblePhrase"]
                # item = self.item(name)
                # item.set_property("visiblePhrase", visiblePhrase)
                # room.add_item(item)
