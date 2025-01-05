from helper_functions import tidy


class Item:

    _name = "Not set"
    _displayName = "Not set"
    _description = "Not set"
    _propertyDicts = []
    _dialogTracker = 0

    def __init__(self, name):
        self._name = name

    def starts_with_vowel(self, word):
        """ returns True if the word starts with a vowel """
        if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
            return True
        return False

    # getters
    def name(self):
        """ getter """
        return self._name

    def name_indef(self):
        """ get the name with an indefinite article in front """
        if self.starts_with_vowel(self._name):
            return str("an " + self.pretty_name())
        return str("a " + self.pretty_name())

    def pretty_name(self):
        """ getter """
        if self.has_property("treasure_value"):
            return str("*** " + self._name + " ***")

        if self.get_property("killed"):
            return str("dead " + self._name)

        return self._name

    def description(self):
        """ getter """
        return self._description

    def has_property(self, prop):
        """ True if the property exists; False if not """
        for pd in self._propertyDicts:
            if prop in pd:
                return True
        return False

    def get_property_dict(self, property_name):
        """ Return's the property's value if it exists; None Type if not """
        for property_dict in self._propertyDicts:
            property = list(property_dict.keys())[0]
            if property == property_name:
                return property_dict
        return None

    def get_property(self, property_name):
        """ Return's the property's value if it exists; None Type if not """
        for property_dict in self._propertyDicts:
            if property_name in property_dict:
                return property_dict[property_name]
        return None

    def gettable(self):
        """ 
        Specifically checks for an item's gettable property. 
        If it doesn't have one, assume it IS gettable.
        """
        gettable = self.get_property("gettable")
        if gettable is None:
            return True
        return gettable

    def propertyDicts(self):
        return self._propertyDicts

    def dialogTracker(self):
        return self._dialogTracker

    def is_treasure(self):
        """ getter """
        if self.get_property("treasure_value") is not None:
            return self.get_property("treasure_value")
        return False

    # setters
    def set_description(self, to_set):
        """ setter"""
        self._description = tidy(to_set)

    def set_property(self, prop, val):
        """ setter """
        for index, pd in enumerate(self._propertyDicts):
            if prop in pd:
                pd[prop] = val
                self._propertyDicts[index] = pd
                return
        print("!!! Couldn't set property (" + str(prop) + ")")
        return

    def setDisplayName(self, s):
        self._displayName = s

    def setPropertyDicts(self, pd):
        self._propertyDicts = pd

    def incrementDialogTracker(self):
        self._dialogTracker = self._dialogTracker + 1
