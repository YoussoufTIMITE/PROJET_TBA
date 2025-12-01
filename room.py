# Define the Room class.
# room.py

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # dictionnaire direction → Room

    def get_long_description(self):
        exits_str = ", ".join([d for d, r in self.exits.items() if r is not None])
        return f"\n{self.name}\n{self.description}\nSorties disponibles : {exits_str}\n"

