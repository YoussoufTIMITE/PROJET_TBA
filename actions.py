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
        
        print("\nVous attendez un moment... Les PNJ se déplacent.\n")
        game.move_npcs()
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
            if npc.name == "Fantome":
                game.ghost_defeated = True
                print("Le Fantôme est vaincu ! Vous pouvez maintenant affronter le Gardien.")
            elif npc.name == "Gardien":
                if game.ghost_defeated:
                    print("Félicitations ! Vous avez vaincu le Gardien et gagné le jeu !")
                    game.finished = True
                else:
                    print("Vous devez d'abord vaincre le Fantôme avant le Gardien !")
                    # Remettre le Gardien en vie ou quelque chose, mais pour simplicité, juste message
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
    
    @staticmethod
    def déplacer(game, list_of_words, number_of_parameters):
        """Déplace un PNJ vers une pièce spécifique"""
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'déplacer' prend 2 paramètres : <pnj> <pièce>.\n")
            return False
        
        npc_name = list_of_words[1]
        room_name = list_of_words[2]
        
        # Trouver le PNJ dans toutes les pièces
        npc = None
        current_room = None
        for room in game.rooms:
            npc = room.get_npc_by_name(npc_name)
            if npc:
                current_room = room
                break
        
        if not npc:
            print(f"\nLe PNJ '{npc_name}' n'existe pas.\n")
            return False
        
        # Trouver la pièce cible
        target_room = None
        for room in game.rooms:
            if room.name.lower() == room_name.lower():
                target_room = room
                break
        
        if not target_room:
            print(f"\nLa pièce '{room_name}' n'existe pas.\n")
            return False
        
        if current_room:
            current_room.remove_npc(npc)
        target_room.add_npc(npc)
        
        print(f"\n{npc.name} a été déplacé vers {target_room.name}.\n")
        return True
    
    @staticmethod
    def listPNJ(game, list_of_words, number_of_parameters):
        """Liste tous les PNJ et leur position"""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False
        
        print("\nListe des PNJ :")
        for room in game.rooms:
            for npc in room.npcs:
                status = "vivant" if npc.is_alive else "mort"
                print(f"  - {npc.name} ({status}) dans {room.name}")
        print()
        return True
    
    @staticmethod
    def use(game, list_of_words, number_of_parameters):
        """Utiliser un objet de l'inventaire"""
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False
        
        item_name = list_of_words[1]
        player = game.player
        
        item = player.get_item_from_inventory(item_name)
        if item is None:
            print(f"\nVous ne possédez pas '{item_name}'.\n")
            return False
        
        # Effets selon l'objet
        if item.name.lower() == "clé":
            print("\nLa clé brille. Elle pourrait ouvrir une porte secrète, mais ici, elle vous rappelle que la vraie clé est de vaincre les PNJ dans l'ordre.\n")
        elif item.name.lower() == "lampe":
            print("\nLa lampe éclaire les recoins sombres. Vous voyez des inscriptions murales : 'Le Fantôme hante les tunnels, le Gardien protège la sortie.'\n")
        elif item.name.lower() == "livre":
            print("\nLe livre contient des légendes anciennes : 'Pour sortir, bats le Fantôme spectral, puis le Gardien immortel.'\n")
        elif item.name.lower() == "torche":
            print("\nLa torche flambe vivement. Sa chaleur vous revigore (+5 PV).\n")
            player.health = min(100, player.health + 5)
        elif item.name.lower() == "corde":
            print("\nLa corde vous permet de grimper à un point élevé. De là, vous voyez les mouvements des PNJ.\n")
            Actions.listPNJ(game, ["listPNJ"], 0)
        elif item.name.lower() == "pioche":
            print("\nLa pioche creuse le sol. Vous trouvez une inscription : 'Le Gardien ne tombe que si le Fantôme est vaincu.'\n")
        else:
            print(f"\nVous utilisez {item.name}, mais rien ne se passe.\n")
        
        return True