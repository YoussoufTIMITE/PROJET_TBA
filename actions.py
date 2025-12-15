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
        if player.move(list_of_words[1]):
            # Déplacer les PNJ après le mouvement du joueur
            game.move_npcs()
            # Afficher la description mise à jour
            print(player.current_room.get_long_description())
            return True
        return False

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
        """ Permet au joueur d'examiner son environnement ou un objet spécifique."""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        
        player = game.player
        print(player.current_room.get_long_description())
        return True
    
    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """Permet au joueur de ramasser un objet."""
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
        """ Permet au joueur de déposer un objet de son inventaire dans l'environnement."""
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
    
    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """Permet au joueur de parler à un PNJ."""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False
        
        npc_name = list_of_words[1]
        player = game.player
        current_room = player.current_room
        
        npc = current_room.get_npc_by_name(npc_name)
        if npc is None:
            print(f"\nLe PNJ '{npc_name}' n'est pas ici.\n")
            return False
        
        print(f"\n{npc.talk()}\n")
        return True
    
    @staticmethod
    def wait(game, list_of_words, number_of_parameters):
        """Permet au joueur d'attendre un tour, faisant bouger les PNJ."""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        
        print("\nVous attendez un moment...\n")
        return True
    
    @staticmethod
    def attack(game, list_of_words, number_of_parameters):
        """Permet au joueur d'attaquer un PNJ."""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False
        
        npc_name = list_of_words[1]
        player = game.player
        current_room = player.current_room
        
        npc = current_room.get_npc_by_name(npc_name)
        if npc is None:
            print(f"\nLe PNJ '{npc_name}' n'est pas ici.\n")
            return False
        
        if not npc.is_alive:
            print(f"\n{npc.name} est déjà vaincu.\n")
            return False
        
        # Attaque du joueur
        damage_to_npc = 20  # dégâts fixes pour simplicité
        result = npc.take_damage(damage_to_npc)
        print(f"\nVous attaquez {npc.name} et infligez {damage_to_npc} dégâts. {result}\n")
        
        if not npc.is_alive:
            current_room.remove_npc(npc)
            if npc.name == "Gardien":
                print("Félicitations ! Vous avez vaincu le Gardien et gagné le jeu !\n")
                game.finished = True
            return True
        
        # Contre-attaque du PNJ
        damage_to_player = 15
        result_player = player.take_damage(damage_to_player)
        print(f"{npc.name} contre-attaque et vous inflige {damage_to_player} dégâts. {result_player}\n")
        
        if player.health <= 0:
            print("Vous êtes mort ! Game over.\n")
            game.finished = True
        
        return True
    
    @staticmethod
    def status(game, list_of_words, number_of_parameters):
        """Affiche l'état du joueur"""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        
        player = game.player
        print(f"\nÉtat de {player.name} : {player.health} PV\n")
        return True