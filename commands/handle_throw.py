from helper_functions import print2


def handle_throw(words, game):
    if len(words) == 1:
        print2("You threw the air.")
    else:
        thing = " ".join(words[1:len(words)])
        item = game.get_item_in_inventory(thing)
        if item is None:
            print2("You don't have that.")
        else:
            do_command(item, game)


def do_command(item, game):
    game.commonActions()
    # you successfully threw the object, so add it to the current room
    game.add_item_to_player_room(item.name())
    game.add_item_to_player_room("dent")
    game.player().removeFromInventory(item)
    print2("You threw the " + item.name() + ". And made a dent! @__@")
