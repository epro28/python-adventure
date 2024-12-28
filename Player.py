from Inventory import Inventory


class Player:

    _inventory = Inventory()
    _name = "Bob Smith"
    _hp = 100

    def addToInventory(self, item):
        self._inventory.add(item)

    def removeFromInventory(self, item):
        self._inventory.remove(item)

    # setters
    def decrementHp(self, amountToDecrement):
        self._hp = self._hp - amountToDecrement

    # getters
    def inventory(self):
        return self._inventory

    def hp(self):
        return self._hp
