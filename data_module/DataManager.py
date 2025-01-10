""" DataManager.py """

import json
import os
from os.path import isfile, join
import copy
from Room import Room
from Item import Item
from Map import Map
from helper_functions import tidy
from data_module.PlayerConfig import PlayerConfig
from data_module.MapConfig import MapConfig
from data_module.DataRoomMisc import DataRoomMisc
from data_module.DataRoomCastleTemplate import DataRoomCastleTemplate
from data_module.DataRoomOutskirtsTemplate import DataRoomOutskirtsTemplate
from data_module.DataRoomEntrance import DataRoomEntrance
from data_module.DataRoomBlueRoom import DataRoomBlueRoom
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
    _map_configs = []
    _inventory_items = []
    _player_position = []
    _map = Map()

    def __init__(self):

        self._map_configs = MapConfig().map_config()
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

        data_items2 = []
        data_path = os.path.join(os.getcwd(), "data")
        for file in os.listdir(data_path):
            if isfile:
                file_name = join(data_path, file)
                print(file_name)
                with open(file_name) as file_data:
                    data = file_data.read()
                    print(data)
                    data_items.append(json.loads(data))

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
        #   2. constructing rooms using simple references to pre-build rooms
        #   3. in both cases, add rooms to map using coordindates

        data_room_templates = self.load_in_template_data()

        self._room_templates = self.make_rooms(
            data_room_templates, data_room_templates)

        data_rooms = self.load_in_room_data()

        self._rooms = self.make_rooms(data_rooms, data_room_templates)

        misc_rooms = self.make_rooms(
            DataRoomMisc().misc_rooms(), data_room_templates)

        for misc_room in misc_rooms:
            self._rooms.append(misc_room)

        # Populate the map with rooms
        for map_config in self._map_configs:
            coordinates = map_config["coordinates"].split(",")
            x = int(coordinates[0])
            y = int(coordinates[1])
            room_name = map_config["name"]
            self._map.add_room(x, y, self.room(room_name))

        for item in self._items:
            print(item.name())

    def make_rooms(self, data_rooms, data_room_templates):
        rooms = []
        for data_room in data_rooms:
            # if there's a template, do a copy of an existing room template;
            # otherwise create the room uniquely
            room = None
            if "template" in data_room:
                for data_room_template in data_room_templates:
                    if data_room["template"] == data_room_template["name"]:
                        room = copy.deepcopy(self.room_template(
                            data_room_template["name"]))
                        pass
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
            DataRoomEntrance().room_data(),
            DataRoomBlueRoom().room_data(),
            DataRoomTrampoline().room_data(),
            DataRoomBasic().room_data(),
            DataRoomBroom().room_data(),
            DataRoomCat().room_data(),
            DataRoomStudy().room_data(),
            DataRoomFrontDoor().room_data(),
        ]
        return data_rooms

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

    def map(self):
        """ getter """
        return self._map

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
        prop = "name"
        if prop in dict:
            room.set_name(dict[prop])

    def set_description_from_data(self, dict, room):
        prop = "description"
        if prop in dict:
            room.set_description(tidy(dict[prop]))

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
                item = Item(data_extra_item["name"])
                item.set_description(data_extra_item["description"])
                item.setPropertyDicts(data_extra_item["property_dicts"])
                room.add_item(item)
                self._items.append(item)
