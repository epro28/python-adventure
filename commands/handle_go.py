from helper_functions import print2


def handle_go(words, game):
    success = False
    if len(words) == 1:
        print2("You gotta say where to go.")
    else:
        thing = " ".join(words[1:len(words)])
        if thing in ("e", "east"):
            success = game.movePlayerEast()
        elif ((thing == "w") or (thing == "west")):
            success = game.movePlayerWest()
        elif ((thing == "s") or (thing == "south")):
            success = game.movePlayerSouth()
        elif ((thing == "n") or (thing == "north")):
            success = game.movePlayerNorth()
        else:
            print2("You can't go there.")
    if success:
        print2("You move to a new room.")
        game.player_room().look()
        game.resetRoomCommandCount()
