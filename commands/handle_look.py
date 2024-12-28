from helper_functions import print2
from helper_functions import remove_junk_words


def handle_look(words, game):
    """ Handle look """

    words = remove_junk_words(words)
    thing = " ".join(words[1:len(words)])
    do_command(thing, game)


def do_command(thing, game):
    """ Handle the command """
    game.commonActions()

    if thing == "":
        # if they didn't specify an object, assume they want to look at the room
        game.player_room().look()

    elif thing in ("e", "east"):
        game.player_room().lookEast()

    elif thing in ("w", "west"):
        game.player_room().lookWest()

    elif thing in ("s", "south"):
        game.player_room().lookSouth()

    elif thing in ("n", "north"):
        game.player_room().lookNorth()

    else:
        # do the looking
        description = None
        item = game.search_inventory(thing)
        if not item is None:
            description = item.description()
        else:
            item = game.search_room(thing)
            if not item is None:
                description = item.description()

        if description is None:
            print2("You don't see that here.")
        else:
            print2(description)
            match thing:
                case "sign":
                    print2("Your score is " + str(game.score()) + ".")
                    for item in game.player_room().items():
                        if item.has_property("treasure_value"):
                            print2(item.pretty_name())
        return

#            else:
#                # the seagull is circling
#                print2(">> There's an angry seagull circling above you! <<")
