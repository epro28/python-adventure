from helper_functions import print2
from helper_functions import print_list


def handle_progress(game):
    print_list("Learned magic words", game.magicWords())
    print_list("Discovered treasures", game.treasures())
    print2("Your score is " + str(game.score()))
    print2("Your HP is " + str(game.player().hp()))
    print2("Number of actions in this room is " + str(game.roomCommandCount()))
    print2("Total number of actions is " + str(game.totalCommandCount()))
