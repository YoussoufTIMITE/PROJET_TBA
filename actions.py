MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
MSG_WRONG_PARAMS = "\nLa commande '{command_word}' prend {expected} paramètre(s).\n"

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
    
    @staticmethod
    def historik(game, list_of_words, number_of_parameters):
        # Vérifie si le nombre d'arguments est correct
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Récupère le joueur actuel et affiche l'historique
        player = game.player
        print("\nHistorique des pièces parcourues :")
        print(player.get_history())
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        # Vérifie si le nombre d'arguments est correct
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        # Besoin d'au moins deux pièces dans l'historique pour revenir en arrière
        if len(player.history) < 2:
            print("\nAucune pièce précédente à laquelle revenir.\n")
            return False

        # Retire la pièce courante de l'historique et revient à la précédente
        player.history.pop()
        previous_room = player.history[-1]
        player.current_room = previous_room
        print(f"\nVous revenez à '{player.current_room.name}'")
        print(player.current_room.get_long_description())
        return True
    
    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """Observer l'environnement"""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        
        player = game.player
        print(player.current_room.get_long_description())
        return True
    
    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """Prendre un objet"""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False
        
        item_name = list_of_words[1]
        player = game.player
        current_room = player.current_room
        
        item = current_room.get_item_by_name(item_name)
        if item is None:
            print(f"\nL'objet '{item_name}' n'est pas ici.\n")
            return False
        
        current_room.remove_item(item)
        player.add_item_to_inventory(item)
        print(f"\nVous avez pris : {item.name}\n")
        return True
    
    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """Poser un objet"""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False
        
        item_name = list_of_words[1]
        player = game.player
        
        item = player.get_item_from_inventory(item_name)
        if item is None:
            print(f"\nVous ne possédez pas '{item_name}'.\n")
            return False
        
        player.remove_item_from_inventory(item)
        player.current_room.add_item(item)
        print(f"\nVous avez posé : {item.name}\n")
        return True
    
    @staticmethod
    def inventory(game, list_of_words, number_of_parameters):
        """Vérifier son inventaire"""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        
        player = game.player
        print(f"\n{player.get_inventory_display()}\n")
        return True