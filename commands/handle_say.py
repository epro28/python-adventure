from helper_functions import print2


def handle_say(words, game):
    if len(words) == 1:
        print2("Um, you gotta say what to say.")
    else:
        thing = " ".join(words[1:len(words)])
        do_command(thing, game)


def do_command(thing, game):
    game.commonActions()
    print2("Saying that appears to have no effect.")
