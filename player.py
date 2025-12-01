# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
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
        self.history.append(next_room.name)
        print(f"\nVous vous déplacez vers {real_dir}...\n")
        print(self.current_room.get_long_description())
        return True
