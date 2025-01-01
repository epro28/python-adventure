""" handle_go.py """

from helper_functions import print2


def handle_go(words, game):
    """ handle command """

    if len(words) == 1:
        print2("You gotta say where to go.")
        return

    thing = " ".join(words[1:len(words)])
    if thing in ("e", "east"):
        game.move_player_east()
    elif thing in ("w", "west"):
        game.move_player_west()
    elif thing in ("s", "south"):
        game.move_player_south()
    elif thing in ("n", "north"):
        game.move_player_north()
    else:
        print2("You can't go there.")
    return
