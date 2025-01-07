""" handle_use.py """

from helper_functions import print2
from helper_functions import extract_things_from_words
from helper_functions import indefinite


def handle_use(words, game):
    """ handle use """

    thing1, thing2 = extract_things_from_words(words)
    if thing1 == "" or thing2 == "":
        print2("Say \"use [something] on [something]\"")
        return

    # make sure the item exists
    item1 = game.get_item_in_inventory_and_room(thing1)
    if item1 is None:
        print2("You don't see " + indefinite(thing1) + " here.")
        return

    # if found, make sure the other item exists
    item2 = game.get_item_in_inventory_and_room(thing2)
    if item2 is None:
        print2("You don't see " + indefinite(thing2) + " here.")
        return

    # make sure property exists
    if not item2.has_property("otherItemName"):
        print2("That had no effect.")
        return

    do_command(thing1, thing2, game)


def do_command(item1, item2, game):
    """ handle the command """

    game.commonActions()

    for pd in item2.propertyDicts():

        # look for the propertyDict that mentions item1

        if not "otherItemName" in pd:
            continue

        if pd["otherItemName"] == item1.name():
            # found the propertyDict that mentions item1
            match list(pd.keys())[0]:
                case "lit":
                    pd = handle_lit_property(pd, item2)
                case "unlocked":
                    pd = handle_unlocked_property(pd, item2)
                case "killed":
                    pd = handle_killed_property(pd, item2)
                case _:
                    print("HANDLE THIS PROPERTY A DIFFERENT WAY")
            return

    print2("That had no effect.")


def handle_killed_property(property_dict, item):
    """ Handle killed property """
    if item.get_property("killed"):
        print2("It's already dead.")
    else:
        # you killed it
        item.set_property("killed", True)
        print2(item.get_property("killedPhrase"))
        item.set_description(item.get_property("killedDescription"))
        item.set_property("getPhrase", item.get_property("killedGetPhrase"))
        item.set_property(
            "visiblePhrase", item.get_property("killedVisiblePhrase"))
    return property_dict


def handle_unlocked_property(d, item):
    """ handle property """
    if d["unlocked"]:
        print2("but it longer has an effect.")
    else:
        # unlock it
        d["unlocked"] = True
        print2("and you heard a click!")
        # update the description
        item.set_description(d["desc"])
    return d


def handle_lit_property(d, item):
    """ handle property """
    prop_state_key = list(d.keys())[0]
    prop_state_val = list(d.values())[0]
    if prop_state_val is True:
        print2("but it's already lit.")
    else:
        # Flip the state
        prop_state_val = True
        d[prop_state_key] = prop_state_val
        # Set the new description
        item.set_description(list(d.values())[2])
        print2(item.description())
    return d
