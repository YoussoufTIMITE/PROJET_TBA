# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = []  # inventaire du joueur
        self.health = 100  # points de vie
        # dictionnaire alias directions
        self.direction_aliases = {
            "N": ["N", "NORD", "NORTH"],
            "E": ["E", "EST", "EAST"],
            "S": ["S", "SUD", "SOUTH"],
            "O": ["O", "OUEST", "WEST"],
            "U": ["U", "UP", "HAUT"],
            "D": ["D", "DOWN", "BAS"]
        }
        # dictionnaire alias directions
        self.direction_aliases = {
            "N": ["N", "NORD", "NORTH"],
            "E": ["E", "EST", "EAST"],
            "S": ["S", "SUD", "SOUTH"],
            "O": ["O", "OUEST", "WEST"],
            "U": ["U", "UP", "HAUT"],
            "D": ["D", "DOWN", "BAS"]
        }

    def normalize_direction(self, direction):
        direction = direction.upper()
        for key, aliases in self.direction_aliases.items():
            if direction in aliases:
                return key
        return None

    def move(self, direction):
        real_dir = self.normalize_direction(direction)
        if real_dir is None:
            print("\nDirection inconnue ! Essayez N, S, E, O, U ou D.\n")
            return False

        if real_dir not in self.current_room.exits:
            print("\nVous ne pouvez pas aller dans cette direction.\n")
            return False

        next_room = self.current_room.exits.get(real_dir)

        if next_room is None:
            print("\nSens unique ! Vous ne pouvez pas aller dans cette direction.\n")
            return False

        # Déplacement valide
        self.current_room = next_room
        self.history.append(next_room)
        print(f"\nVous vous déplacez vers {real_dir}...\n")
        # Ne pas print la description ici, le faire dans Actions.go après mouvement des PNJ
        return True

    def get_history(self):
        if not self.history:
            return "(aucune pièce visitée)"
        # Retourne une chaîne lisible des noms de pièces visitées
        return " -> ".join([room.name for room in self.history])
    
    def add_item_to_inventory(self, item):
        """Ajoute un objet à l'inventaire du joueur"""
        self.inventory.append(item)
    
    def remove_item_from_inventory(self, item):
        """Retire un objet de l'inventaire du joueur"""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def get_item_from_inventory(self, name):
        """Retourne l'objet correspondant au nom ou None"""
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item
        return None
    
    def get_inventory_display(self):
        """Retourne une chaîne affichant l'inventaire"""
        if not self.inventory:
            return "Votre inventaire est vide."
        items_str = ", ".join([item.name for item in self.inventory])
        return f"Inventaire : {items_str}"
    
    def take_damage(self, damage):
        """Inflige des dégâts au joueur"""
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} est mort !"
        return f"{self.name} a {self.health} PV restants."
