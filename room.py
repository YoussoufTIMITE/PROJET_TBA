# Define the Room class.
# room.py

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # dictionnaire direction → Room
        self.items = []  # inventaire de la pièce
        self.npcs = []  # PNJ dans la pièce

    def get_long_description(self):
        exits_str = ", ".join([d for d, r in self.exits.items() if r is not None])
        description = f"\n{self.name}\n{self.description}\nSorties disponibles : {exits_str}"
        
        # Ajouter les items visibles dans la pièce
        if self.items:
            items_str = ", ".join([item.name for item in self.items])
            description += f"\nObjets visibles : {items_str}"
        
        # Ajouter les PNJ visibles dans la pièce
        if self.npcs:
            npcs_str = ", ".join([npc.name for npc in self.npcs])
            description += f"\nPNJ présents : {npcs_str}"
        
        description += "\n"
        return description
    
    def add_item(self, item):
        """Ajoute un objet à la pièce"""
        self.items.append(item)
    
    def remove_item(self, item):
        """Retire un objet de la pièce"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def get_item_by_name(self, name):
        """Retourne l'objet correspondant au nom ou None"""
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
    
    def add_npc(self, npc):
        """Ajoute un PNJ à la pièce"""
        self.npcs.append(npc)
        npc.move_to_room(self)
    
    def remove_npc(self, npc):
        """Retire un PNJ de la pièce"""
        if npc in self.npcs:
            self.npcs.remove(npc)
            return True
        return False
    
    def get_npc_by_name(self, name):
        """Retourne le PNJ correspondant au nom ou None"""
        for npc in self.npcs:
            if npc.name.lower() == name.lower():
                return npc
        return None

