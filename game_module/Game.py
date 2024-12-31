from Player import Player
from Map import Map
from helper_functions import print2


class Game:

    _dm = None  # Data Manager
    _map = Map()
    _player = None
    _magicWords = ["abracadabra"]
    _treasures = []
    _score = 0
    _roomCommandCount = 0
    _totalCommandCount = 0

    def __init__(self, dm):

        self._dm = dm

        self._player = Player()

        # Give items to the player
        for inventory_item in self._dm.inventory_items():
            self._player.addToInventory(self._dm.item(inventory_item))

        # Populate the map with rooms
        for map_room in self._dm.map_rooms():
            room_name = map_room["room_name"]
            coordinates = map_room["coordinates"].split(",")
            # item_names = map_room["item_names"]
            x = int(coordinates[0])
            y = int(coordinates[1])
            self._map.addRoom(x, y, self._dm.room(room_name))
            # for item_name in item_names:
            #    self._map.add_item_to_room(self._dm.item(item_name), room_name)

        self._map.player_room().setVisited(True)

    def is_item_in_inventory(self, item_name):
        """ True if the item is in the players inventory; otherwise False """
        if self.get_item_in_inventory(item_name) is None:
            return False
        return True

    def is_item_in_room(self, item_name):
        """ True if the item is in the players room; otherwise False """
        if self.get_item_in_room(item_name) is None:
            return False
        return True

    def get_item_in_room(self, object_name):
        """ return item if found; otherwise return None """
        item = self.player_room().find(object_name)
        return item

    def get_item_in_inventory(self, object_name):
        """ return item if found; otherwise return None """
        item = self.player().inventory().find(object_name)
        return item

    def get_item_in_inventory_and_room(self, object_name):
        """ return item if found; otherwise return None """
        item = self.get_item_in_inventory(object_name)
        if (item is None):
            item = self.get_item_in_room(object_name)
        return item

    def commonActions(self):
        self.incrementRoomCommandCount()
        self.incrementTotalCommandCount()

    def checkAndMoveRooms(self, x, y):
        success = False
        nextRoom = self._map.roomWithLocation(x, y)
        if nextRoom is None:
            print2("There is no room in that direction.")
        else:
            self._map.setPlayerLocation(x, y)
            # self._currentRoom = nextRoom
            self.player_room().setVisited(True)
            success = True
        return success

    def do_move(self, door, x, y):
        if door is None:
            print2("You see nowhere to go in that direction.")
            return False

        if "locked" in door and door["locked"]:
            print2("You see a door, but it's locked.")
            return False

        return self.checkAndMoveRooms(x, y)

    def movePlayerEast(self):
        return self.do_move(
            self.player_room().eastDoor(),
            self._map.playerX()+1,
            self._map.playerY())

    def movePlayerWest(self):
        return self.do_move(
            self.player_room().westDoor(),
            self._map.playerX()-1,
            self._map.playerY())

    def movePlayerNorth(self):
        return self.do_move(
            self.player_room().northDoor(),
            self._map.playerX(),
            self._map.playerY()-1)

    def movePlayerSouth(self):
        return self.do_move(
            self.player_room().southDoor(),
            self._map.playerX(),
            self._map.playerY()+1)

    def handle_revealed_item(self, main_item, revealed_dict):
        """ Handle revealed item """
        item = self._dm.item(revealed_dict["name"])
        print(item)
        item.set_property("visible", True)
        if self.is_item_in_room(main_item.name()):
            self.add_item_to_player_room(item.name())
        elif self.is_item_in_inventory(main_item.name()):
            self.addItemToPlayer(item.name())
        else:
            print("!!! Revealed item is not in room or with player (" + item.name() + ")")
        print2(revealed_dict["revealedPhrase"])

    def handle_seagull(self):
        """ handle the case of a seagull being in the player's room """

        seagull = self.get_item_in_room("seagull")
        if seagull is None:
            return

        # there's a seagull in the room

        if seagull.has_property("killed") and not seagull.get_property("killed"):

            # the seagull is alive

            if self.roomCommandCount() == 5:
                # time for the seagull to swoop down
                self.resetRoomCommandCount()
                hp_lost = 5
                self.player().decrementHp(hp_lost)
                print2(">> The seagull swoops down and hits you in the coconut! <<")
                print2(">> You lost " + str(hp_lost) + " HP! (" +
                       str(self.player().hp()) + " remaining) <<")

    # GAME / PLAYER INTERACTIONS

    def addItemToPlayer(self, itemName):
        self._player.addToInventory(self._dm.item(itemName))

    def removeItemFromPlayer(self, itemName):
        self._player.removeFromInventory(self._dm.item(itemName))

    # GAME / MAP INTERACTIONS

    def add_item_to_player_room(self, item_name):
        """ add item specifically to the player's room """
        self._map.add_item_to_player_room(self._dm.item(item_name))

    def add_item_to_room(self, item_name, room_name):
        """ add item to room using their names """
        self._map.add_item_to_room(self._dm.item(item_name), room_name)

    def remove_item_from_player_room(self, item_name):
        """ remove item from player room """
        self._map.remove_item_from_player_room(item_name)

    def removeItemFromRoom(self, itemName, roomName):
        self._map.removeItemFromRoom(
            self._dm.item(itemName), self._dm.room(roomName))

    def incrementRoomCommandCount(self):
        self._roomCommandCount = self._roomCommandCount + 1

    def resetRoomCommandCount(self):
        self._roomCommandCount = 0

    def incrementTotalCommandCount(self):
        self._totalCommandCount = self._totalCommandCount + 1

    def increment_score(self, to_set):
        """ setter """
        self._score = self._score + int(to_set)

    # Getters
    def map(self):
        return self._map

    def player(self):
        return self._player

    def player_room(self):
        return self._map.player_room()

    def magicWords(self):
        return self._magicWords

    def treasures(self):
        return self._treasures

    def score(self):
        """ getter """
        return self._score

    def roomCommandCount(self):
        return self._roomCommandCount

    def totalCommandCount(self):
        return self._totalCommandCount
