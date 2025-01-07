""" handle_look.py """

from helper_functions import print2
from helper_functions import remove_junk_words
from helper_functions import indefinite


def handle_look(words, game):
    """ handle command """

    words = remove_junk_words(words)
    thing = " ".join(words[1:len(words)])

    if thing == "":
        # if they didn't specify an object, assume they want to look at the room
        game.player_room().look()
        return

    if thing in ("e", "east"):
        game.player_room().look_east()
        return

    if thing in ("w", "west"):
        game.player_room().look_west()
        return

    if thing in ("s", "south"):
        game.player_room().look_south()
        return

    if thing in ("n", "north"):
        game.player_room().look_north()
        return

    # make sure the item exists
    item = game.get_item_in_inventory_and_room(thing)
    if item is None:
        print2("You don't see " + indefinite(thing) + " here.")
        return

    do_command(item, game)


def do_command(item, game):
    """ handle the command """

    game.commonActions()

    print2(item.description())

    looked_property_dict = item.get_property_dict("looked")

    if not looked_property_dict is None:
        if looked_property_dict["looked"] is False:
            looked_property_dict["looked"] = True
            game.handle_revealed_item(item, looked_property_dict)

    match item.name():
        case "sign":
            print2("Your score is " + str(game.score()) + ".")
            for anitem in game.player_room().items():
                if anitem.has_property("treasure_value"):
                    print2(anitem.pretty_name())
    return
