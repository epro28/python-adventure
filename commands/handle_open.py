from helper_functions import print2


def handle_open(words, game):

    if len(words) == 1:
        print2("You gotta say what to open.")
    else:
        thing = " ".join(words[1:len(words)])
        item = game.search_inventory_and_room(thing)
        if item is None:
            print2("You don't see that here.")
        else:
            do_command(item, game)


def do_command(item, game):
    """ Handle the command """
    game.commonActions()

    # make sure property exists
    if not item.has_property("opened"):
        print2("You can't open it.")

    # if so, handle it and any associated properties
    else:

        for property_dict in item.propertyDicts():
            prop = list(property_dict.keys())[0]
            match prop:
                case "opened":
                    success = True
                    property_dict = handle_opened_property(
                        property_dict, item, game)
                case "unlocked":
                    success = True
                    if item.get_property("unlocked") is False:
                        print2("It's locked.")
                case _:
                    success = True
                    print("HANDLE THIS PROPERTY A DIFFERENT WAY (" + prop + ")")
        if not success:
            print2("Nothing happened.")


def handle_opened_property(property_dict, item, game):
    """ Handle opened property """
    if property_dict["opened"] is True:
        print2("It's already open.")
    else:
        property_dict["opened"] = True
        item.set_description(property_dict["desc"])
        print2("You opened it...")
        game.handle_revealed_item(property_dict, item.description())
    return property_dict
