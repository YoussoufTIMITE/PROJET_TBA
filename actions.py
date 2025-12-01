MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False

        # APPEL UNIQUEMENT À move(), qui gère tout
        return player.move(list_of_words[1])

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        print(f"\nMerci {game.player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        print("\nVoici les commandes disponibles :")
        for command in game.commands.values():
            print(f"  - {command}")
        print()
        return True
