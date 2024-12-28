from helper_functions import print2
from helper_functions import remove_junk_words


def handle_drop(words, game):
    """ Handle drop """

    words = remove_junk_words(words)
    thing = " ".join(words[1:len(words)])
    if thing == "":
        print2("Say \"Drop [Something]\"")
        return
    do_command(thing, game)


def do_command(thing, game):
    """ Handle the command """
    game.commonActions()

    # make sure you're holding it
    item = game.search_inventory(thing)
    if item is None:
        print2("You don't have a " + thing + ".")
        return

    # drop it
    game.removeItemFromPlayer(item.name())
    game.addItemToplayer_room(item.name())
    print2("You dropped the " + item.name() + ".")

    if item.is_treasure() and game.player_room().is_treasure_room():
        game.increment_score(item.get_property("treasure_value"))
        item.set_property("gettable", False)
        print2("For a split second the sign glowed with a platinum light.")
