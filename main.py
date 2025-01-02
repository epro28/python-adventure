import sys
import datetime
from game_module.Game import Game
from commands.CommandHandler import CommandHandler
from commands.handle_look import handle_look
from data_module.DataManager import DataManager
from helper_functions import print_terminal_lines


LOG_COMMANDS = False


def write_to_command_log(to_write):
    """ log commands to a file """
    file = open("commandLog.txt", "a")
    file.write(to_write)
    file.close()


print(sys.argv)
if not (len(sys.argv) > 1 and sys.argv[1] == "jk"):
    LOG_COMMANDS = True
    write_to_command_log("\n")
    write_to_command_log(str(datetime.datetime.now()) + "\n")

# Execute the Game
print("")  # print a blank line
print("=====================================================")
print("==                                                 ==")
print("==    Welcome to the Adventure of Your Lifetime    ==")
print("==                                                 ==")
print("=====================================================")
print("")

dm = DataManager()

_game = Game(dm)
_commandHandler = CommandHandler(dm)

FIRST_TIME = True
while True:

    if FIRST_TIME:
        # print_terminal_lines("\n==")
        # handle_look(["look"], _game)
        # print("==")
        # print_terminal_lines("")
        FIRST_TIME = False

    print("")  # add a blank line

    # Get the user's input
    user_input = input("Enter your command: ")
    user_input = user_input.lower()  # convert to lower case

    if LOG_COMMANDS:
        write_to_command_log(user_input + "\n")

    # Break the input into pieces
    words = user_input.split(" ")

    # Handle the command
    # object, objectJoiner, object2, _game)
    SHOULD_EXIT = _commandHandler.handle_command(words, _game)

    if SHOULD_EXIT:
        break

print("Bye.")
print("")
