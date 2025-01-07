import textwrap
import re

_maxLineLength = 60
_junk_words = ["on", "with", "in", "to", "at", "the", "a"]
_vowels = ["a", "e", "i", "o", "u"]


def starts_with_vowel(word):
    """ returns True if the word starts with a vowel """
    if word[0] in _vowels:
        return True
    return False


def indefinite(string):
    """ convert a noun to its indefinite form """
    if starts_with_vowel(string):
        return str("an " + string)
    return str("a " + string)


def tidy(string):
    """ removes consecutive whitespaces from a string """
    return re.sub(' +', ' ', string)


def remove_junk_words(word_list):
    """ Remove junk words """
    for junk_word in _junk_words:
        try:
            word_list.remove(junk_word)
        except ValueError:
            pass
    return word_list


def extract_things_from_words(word_list):
    """ from what the user entered, figure out the object(s) of the command """
    thing1 = ""
    thing2 = ""
    for junk_word in _junk_words:
        if junk_word in word_list:
            thing1 = " ".join(word_list[1:word_list.index(junk_word)])
            thing2 = " ".join(
                word_list[word_list.index(junk_word)+1:len(word_list)])
            break
    return thing1, thing2


def print2(toPrint):
    wrappedLines = textwrap.wrap(toPrint, width=_maxLineLength)
    for wrappedLine in wrappedLines:
        print("==\t" + wrappedLine)


def print_list(list_name, my_list):
    if (len(my_list) < 1):
        print2("You have no " + list_name.lower())
    else:
        to_print = list_name + " are: "
        for thing in my_list:
            to_print = to_print + thing + ", "
        to_print = to_print[:-2]  # remove the ", " from the last one
        print2(to_print)


def print_terminal_lines(final_char):
    """ for displaying the borders in the terminal window """
    for _ in range(_maxLineLength+15):
        print("=", end="")
    print(final_char)


def last_word_in_string(string):
    """ last word in string """
    # split string into parts
    strings = string.split(" ")
    last_string = strings[len(strings)-1]
    return last_string


def find_item_in_list(item_name, item_list):
    """ find item in list of items """
    found_item = None
    for item in item_list:
        if item_name == item.name() or item_name == last_word_in_string(item.name()):
            found_item = item
            break  # stop searching
    return found_item


def pretty_list(start_phrase, item_list):
    """ print a list of items in a natural style """
    to_print = start_phrase
    if len(item_list) == 1:
        to_print = to_print + indefinite(item_list[0].pretty_name())
    elif len(item_list) == 2:
        to_print = to_print + \
            indefinite(item_list[0].pretty_name()) + \
            " and " + indefinite(item_list[1].pretty_name())
    else:
        for index, item in enumerate(item_list):
            to_print = to_print + item.name_indef()
            if index == len(item_list)-2:
                to_print = to_print + ", and "
            else:
                to_print = to_print + ", "
        to_print = to_print[:-2]  # remove the ", " from the last item
    to_print = to_print + "."
    return to_print
