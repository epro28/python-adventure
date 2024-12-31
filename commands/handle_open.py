""" handle_open.py """
from helper_functions import print2


def handle_open(words, game):
    """ handle open """

    if len(words) == 1:
        print2("You gotta say what to open.")
        return

    thing = " ".join(words[1:len(words)])

    # make sure the item exists
    item = game.get_item_in_inventory_and_room(thing)
    if item is None:
        print2("You don't see that here.")
        return

    # make sure property exists
    if not item.has_property("opened"):
        print2("You can't open it.")
        return

    do_command(item, game)


def do_command(item, game):
    """ Handle the command """

    game.commonActions()

    # handle it and any associated properties
    for property_dict in item.propertyDicts():
        prop = list(property_dict.keys())[0]
        match prop:
            case "visible":
                if not item.get_property("visible"):
                    print2("You don't see that here.")
                    return
            case "unlocked":
                if not item.get_property("unlocked"):
                    print2("It's locked.")
                    return
            case "opened":
                if item.get_property("opened"):
                    print2("It's already open.")
                    return
                else:
                    property_dict = handle_opened_property(
                        property_dict, item, game)
                    return
            case _:
                success = True
                print("HANDLE THIS PROPERTY A DIFFERENT WAY (" + prop + ")")
    print2("Nothing happened.")


def handle_opened_property(property_dict, item, game):
    """ Handle opened property """
    property_dict["opened"] = True
    item.set_description(property_dict["desc"])
    game.handle_revealed_item(item, property_dict["revealedItem"])
    return property_dict
