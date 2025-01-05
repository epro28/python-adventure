""" handle_open.py """
from helper_functions import print2
from helper_functions import remove_junk_words


def handle_open(words, game):
    """ handle open """

    words = remove_junk_words(words)
    thing = " ".join(words[1:len(words)])
    if thing == "":
        print2("Say \"opem [something]\"")
        return

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
    """ handle the command """

    game.commonActions()

    unlocked_property_dict = item.get_property_dict("unlocked")
    if not unlocked_property_dict is None:
        if unlocked_property_dict["unlocked"] is False:
            print2("It's locked.")
            return

    opened_property_dict = item.get_property_dict("opened")

    if opened_property_dict["opened"] is True:
        print2("It's already open.")
        return

    opened_property_dict["opened"] = True
    item.set_description(opened_property_dict["desc"])
    game.handle_revealed_item(item, opened_property_dict)

    """
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
                    return
            case _:
                success = True
                print("HANDLE THIS PROPERTY A DIFFERENT WAY (" + prop + ")")
    print2("Nothing happened.")
    """
