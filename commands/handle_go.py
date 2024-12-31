from helper_functions import print2


def handle_go(words, game):
    success = False
    if len(words) == 1:
        print2("You gotta say where to go.")
    else:
        thing = " ".join(words[1:len(words)])
        if thing in ("e", "east"):
            success = game.movePlayerEast()
        elif thing in ("w", "west"):
            success = game.movePlayerWest()
        elif thing in ("s", "south"):
            success = game.movePlayerSouth()
        elif thing in ("n", "north"):
            success = game.movePlayerNorth()
        else:
            print2("You can't go there.")
    if success:
        game.player_room().look()
        game.resetRoomCommandCount()
