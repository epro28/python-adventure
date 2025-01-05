from helper_functions import print2
from helper_functions import print_list
from helper_functions import print_terminal_lines
from commands.handle_drop import handle_drop
from commands.handle_open import handle_open
from commands.handle_look import handle_look
from commands.handle_get import handle_get
from commands.handle_move import handle_move
from commands.handle_progress import handle_progress
from commands.handle_use import handle_use
from commands.handle_throw import handle_throw
from commands.handle_say import handle_say
from commands.handle_go import handle_go
from commands.handle_talk import handle_talk


class CommandHandler:

    _commands = []
    _commands.append("quit")
    _commands.append("help")
    _commands.append("say")
    _commands.append("look")
    _commands.append("inventory")
    _commands.append("drop")
    _commands.append("get")
    _commands.append("move")
    _commands.append("open")
    _commands.append("throw")
    _commands.append("go")
    _commands.append("hit")
    _dm = None

    def __init__(self, dm):
        self._dm = dm

    # command,object,objectJoiner,object2,game):
    def handle_command(self, words, game,):
        """ handle command """
        print_terminal_lines("\n==")

        shouldExit = False

        if (len(words) == 0):
            print2("Um what?")
            return False
        else:
            command = words[0]

        match command:
            case "quit":
                shouldExit = True
            case "drop":
                handle_drop(words, game)
            case "open":
                handle_open(words, game)
            case "get":
                handle_get(words, game)
            case "move":
                handle_move(words, game)
            case "look":
                handle_look(words, game)
                # print("(" + str(game.map().playerX()) +
                #      "," + str(game.map().playerY()) + ")")
            case "help":
                print_list("Possible commands", self._commands)
            case "progress":
                handle_progress(game)
            case "hi" | "hey":
                print2("Hi.")
            case "jump":
                print2("Wheeeeeee!")
            case "map":
                game.map().show()
            case "inventory" | "i":
                game.player().inventory().look()
            case "use":
                handle_use(words, game)
            case "throw":
                handle_throw(words, game)
            case "say":
                handle_say(words, game)
            case "go":
                handle_go(words, game)
            case "talk":
                handle_talk(words, game)
            case _:
                print2("I don't understand.")

        game.handle_seagull()

        print("==")
        print_terminal_lines("")

        return shouldExit
