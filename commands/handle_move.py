from helper_functions import print2
from helper_functions import remove_junk_words


def handle_move(words, game):
    """ handle move """

    words = remove_junk_words(words)
    thing = " ".join(words[1:len(words)])
    if thing == "":
        print2("Say \"move [something]\"")
        return

    # make sure the item exists
    item = game.get_item_in_inventory_and_room(thing)
    if item is None:
        print2("You don't see that here.")
        return

    # make sure property exists
    if not item.has_property("moved"):
        print2("You can't move it.")
        return

    do_command(item, game)


def do_command(item, game):
    """ handle the command """

    game.commonActions()

    moved_property_dict = item.get_property_dict("moved")
    if moved_property_dict is None:
        print2("That had no effect.")
        return

    if moved_property_dict["moved"] is True:
        print2("You already moved it.")
        return

    moved_property_dict["moved"] = True
    item.set_description(moved_property_dict["desc"])
    game.handle_revealed_item(item, moved_property_dict)
