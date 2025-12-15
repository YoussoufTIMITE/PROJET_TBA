
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from npc import NPC
import random

class Game:

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.ghost_defeated = False

    def setup(self):
        # Commands
        self.commands["help"] = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["go"] = Command("go", " <direction> : se déplacer", Actions.go, 1)
        self.commands["historik"] = Command("historik", " : afficher l'historique des pièces", Actions.historik, 0)
        self.commands["back"] = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["look"] = Command("look", " : observer l'environnement", Actions.look, 0)
        self.commands["take"] = Command("take", " <objet> : prendre un objet", Actions.take, 1)
        self.commands["drop"] = Command("drop", " <objet> : poser un objet", Actions.drop, 1)
        self.commands["inventory"] = Command("inventory", " : vérifier son inventaire", Actions.inventory, 0)
        self.commands["talk"] = Command("talk", " <pnj> : parler à un PNJ", Actions.talk, 1)
        self.commands["wait"] = Command("wait", " : attendre un tour (fait bouger les PNJ)", Actions.wait, 0)
        self.commands["attack"] = Command("attack", " <pnj> : attaquer un PNJ", Actions.attack, 1)
        self.commands["status"] = Command("status", " : vérifier votre état", Actions.status, 0)
        self.commands["déplacer"] = Command("déplacer", " <pnj> <pièce> : déplacer un PNJ vers une pièce", Actions.déplacer, 2)
        self.commands["listPNJ"] = Command("listPNJ", " : lister tous les PNJ et leur position", Actions.listPNJ, 0)
        self.commands["use"] = Command("use", " <objet> : utiliser un objet de l'inventaire", Actions.use, 1)

        # Rooms
        entree = Room("Entrée", "à l’entrée de votre univers. Une lourde porte se referme derrière vous.")
        hall = Room("Hall", "dans un grand hall froid et silencieux.")
        bureau = Room("Bureau", "dans un bureau poussiéreux rempli de vieux dossiers.")
        mezzanine = Room("Mezzanine", "sur une plateforme surplombant le hall.")
        souterrain = Room("Souterrain", "dans un tunnel sombre où règne une odeur d'humidité.")
        cave = Room("Cave", "dans une cave moisie pleine de tonneaux.")
        labyrinthe = Room("Labyrinthe", "dans un couloir sinueux qui semble changer de forme.")
        chambre_gardien = Room("Chambre du gardien", "dans une petite chambre austère éclairée par une bougie.")

        self.rooms.extend([entree, hall, bureau, mezzanine,
                           souterrain, cave, labyrinthe, chambre_gardien])

        # Items - ajout d'objets dans les pièces
        cle = Item("clé", "une vieille clé rouillée")
        lampe = Item("lampe", "une lampe de poche")
        livre = Item("livre", "un vieux livre poussiéreux")
        torche = Item("torche", "une torche éteinte")
        corde = Item("corde", "une corde solide")
        pioche = Item("pioche", "une pioche usée")
        
        entree.add_item(cle)
        hall.add_item(lampe)
        bureau.add_item(livre)
        mezzanine.add_item(torche)
        souterrain.add_item(corde)
        cave.add_item(pioche)

        # NPCs
        gardien = NPC("Gardien", "un homme âgé avec une clé", ["Tu as vaincu le Fantôme ? Prouve-le en me battant.", "Je suis le dernier obstacle.", "Vaincs-moi pour gagner !"])
        gardien.health = 100  # plus de vie pour le boss
        marchand = NPC("Marchand", "un commerçant ambulant", ["Trouve le Fantôme dans le Souterrain et bats-le.", "Puis cherche le Gardien dans sa Chambre pour le vaincre.", "Bats les deux pour t'échapper !"])
        fantome = NPC("Fantome", "une apparition translucide", ["Je suis l'esprit du labyrinthe. Bats-moi pour avancer.", "Le Gardien t'attend après moi.", "Vaincs-nous deux pour gagner."])
        fantome.health = 30  # moins de vie

        chambre_gardien.add_npc(gardien)
        hall.add_npc(marchand)
        souterrain.add_npc(fantome)

        # Exits
        entree.exits = {"N": hall}
        hall.exits = {"S": None, "E": bureau, "U": mezzanine, "O": labyrinthe}
        mezzanine.exits = {"D": hall}
        bureau.exits = {"O": hall, "D": souterrain}
        souterrain.exits = {"U": bureau, "S": cave}
        cave.exits = {"N": labyrinthe, "E": chambre_gardien}
        labyrinthe.exits = {"E": hall, "S": chambre_gardien}
        chambre_gardien.exits = {"O": cave}

        # Player
        name = input("Entrez votre nom: ")
        self.player = Player(name)
        self.player.current_room = entree
        # stocke l'objet Room dans l'historique
        self.player.history.append(entree)

    def move_npcs(self):
        """Déplace les PNJ de manière aléatoire, sauf dans la pièce actuelle du joueur"""
        for room in self.rooms:
            if room != self.player.current_room:
                for npc in room.npcs[:]:  # copie pour éviter modification pendant itération
                    if room.exits and random.random() < 0.2:  # 20% chance de bouger
                        direction = random.choice(list(room.exits.keys()))
                        next_room = room.exits[direction]
                        if next_room is not None:
                            room.remove_npc(npc)
                            next_room.add_npc(npc)
                            print(f"{npc.name} se déplace de {room.name} vers {next_room.name}.")

    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans cette aventure mystérieuse !")
        print("Vous êtes piégé dans un labyrinthe. Parlez au Marchand pour des indices.")
        print("Vainquez d'abord le Fantôme, puis le Gardien pour gagner !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

    def process_command(self, command_string):
        if command_string.strip() == "":
            print("\nAucune commande. Entrez 'help' pour voir les commandes disponibles.\n")
            return

        words = command_string.split()
        command_word = words[0]

        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' inconnue. Entrez 'help' pour la liste.\n")
            return

        self.commands[command_word].execute(self, words)

    def play(self):
        """Lance l'action principale associée à l'objet"""
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

def main():
    """ Point d'entrée principal du programme."""
    Game().play()
if __name__ == "__main__":
    main()
