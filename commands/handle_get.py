from helper_functions import print2
from helper_functions import remove_junk_words


def handle_get(words, game):
    """ Handle get """

    words = remove_junk_words(words)
    thing = " ".join(words[1:len(words)])
    if thing == "":
        print2("Say \"Get [Something]\"")
        return
    do_command(thing, game)


def do_command(thing, game):
    """ Handle the command """
    game.commonActions()

    # make sure it's in the room
    item = game.search_room(thing)
    if item is None:
        print2("There isn't a " + thing + " in this room.")
        return

    # get it
    if item.gettable() is True:
        game.remove_item_from_player_room(item.name())
        game.addItemToPlayer(item.name())
        print2("You got the " + item.name() + ".")
    else:
        print2(item.get_property("getPhrase"))
