from helper_functions import print2


class Map:

    _grid = []
    _numRows = 4
    _numCols = 3
    _playerX = 0
    _playerY = 0

    def __init__(self):

        # Initialize a 2D list
        self._grid = [[0 for x in range(self._numCols)]
                      for x in range(self._numRows)]
        for i in range(self._numRows):
            for j in range(self._numCols):
                self._grid[i][j] = None

    def addRoom(self, i, j, room):
        self._grid[i][j] = room

    def set_treasure_room(self, room_name):
        self.roomWithName(room_name).set_treasure_room("True")

    def addItemToRoom(self, item, roomName):
        self.roomWithName(roomName).addItem(item)

    def addItemToplayer_room(self, item):
        self.player_room().addItem(item)

    def removeItemFromRoom(self, itemName, room):
        room.removeItem(itemName)

    def remove_item_from_player_room(self, item_name):
        """ remove item from player room """
        self.player_room().removeItem(item_name)

    def show(self):

        # print top of map
        to_print = ""
        for i in range(self._numRows):
            to_print = to_print + "-----"
            if i < self._numRows-1:
                to_print = to_print + "-"
        print2(to_print)

        # print cells
        for j in range(self._numCols):
            toPrint = ""
            for i in range(self._numRows):
                if i == self._playerX and j == self._playerY:
                    toPrint = toPrint + "| o |"
                elif self.visitedRoom(i, j):
                    toPrint = toPrint + "| ✓ |"
                else:
                    toPrint = toPrint + "|   |"
                # print gap between cells
                if i < self._numRows-1:
                    if self.visitedRoom(i, j) and self.visitedRoom(i+1, j):
                        toPrint = toPrint + "-"
                    else:
                        toPrint = toPrint + " "
            print2(toPrint)

            # print separator between rows
            if j < self._numCols-1:
                toPrint = ""
                for i in range(self._numRows):
                    if self.visitedRoom(i, j) and self.visitedRoom(i, j+1):
                        toPrint = toPrint + "--|--"
                    else:
                        toPrint = toPrint + "-----"
                    if i < self._numRows-1:
                        toPrint = toPrint + "-"
                print2(toPrint)

        # print bottom of map
        toPrint = ""
        for i in range(self._numRows):
            toPrint = toPrint + "-----"
            if i < self._numRows-1:
                toPrint = toPrint + "-"
        print2(toPrint)

    # setters
    def setPlayerLocation(self, x, y):
        self._playerX = x
        self._playerY = y

    # getters
    def playerX(self):
        return self._playerX

    def playerY(self):
        return self._playerY

    def roomWithName(self, name):
        for i in range(self._numRows):
            for j in range(self._numCols):
                room = self._grid[i][j]
                if (not room is None) and (room.name() == name):
                    return room
        print("!!! Couldn't find room in map")
        return None

    def roomWithLocation(self, x, y):
        # return self._grid[x][y]
        return self.checkAndGetRoom(x, y)

    def player_room(self):
        return self._grid[self._playerX][self._playerY]

    def checkAndGetRoom(self, x, y):
        if x < 0 or x > self._numRows-1 or y < 0 or y > self._numCols+1:
            return None
        else:
            return self._grid[x][y]

    def playerEastRoom(self):
        return self.checkAndGetRoom(self._playerX+1, self._playerY)

    def playerWestRoom(self):
        return self.checkAndGetRoom(self._playerX-1, self._playerY)

    def playerNorthRoom(self):
        return self.checkAndGetRoom(self._playerX, self._playerY-1)

    def playerSouthRoom(self):
        return self.checkAndGetRoom(self._playerX, self._playerY+1)

    def eastRoom(self, x, y):
        return self.checkAndGetRoom(x+1, y)

    def westRoom(self, x, y):
        return self.checkAndGetRoom(x-1, y)

    def northRoom(self, x, y):
        return self.checkAndGetRoom(x, y-1)

    def southRoom(self, x, y):
        return self.checkAndGetRoom(x, y+1)

    def visitedRoom(self, x, y):
        if (not self.roomWithLocation(x, y) is None) and (self.roomWithLocation(x, y).visited()):
            return True
        else:
            return False
