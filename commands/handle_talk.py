from helper_functions import print2
from helper_functions import remove_junk_words
from helper_functions import indefinite


def handle_talk(words, game):
    """ Handle talk """

    words = remove_junk_words(words)
    thing = " ".join(words[1:len(words)])
    if thing == "":
        print2("Say \"Use [Something] on [Something]\"")
        return
    do_command(thing, game)


def do_command(thing, game):
    """ Handle the command """
    game.commonActions()

    # make sure it's in the room
    item = game.get_item_in_inventory_and_room(thing)
    if item is None:
        print2("You don't see " + indefinite(thing) + " here.")
        return

    # make sure you can talk to it
    if not item.get_property("talkable") is True:
        print2("The " + item.name() +
               " isn't interested in what you have to say.")
        return

    talkable_state = item.get_property("talkable")

    # handle if its possible to talk, but...
    if talkable_state is False:
        print2("You think the " + item.name() +
               " hears you, but for some reason doesn't respond.")
        return

    # do the talking
    dialog = item.get_property("dialog")
    dialog_length = len(dialog)
    if item.dialogTracker() < dialog_length:
        print2(dialog[item.dialogTracker()])
        if not item.dialogTracker() == dialog_length - 1:
            item.incrementDialogTracker()
        return

    print("!!! No dialog lines??")
