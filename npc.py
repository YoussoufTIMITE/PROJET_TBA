# npc.py

class NPC:
    def __init__(self, name, description, dialogues=None):
        self.name = name
        self.description = description
        self.current_room = None
        self.dialogues = dialogues or ["Bonjour, je n'ai rien à dire."]
        self.dialogue_index = 0
        self.health = 50  # points de vie
        self.is_alive = True

    def talk(self):
        """Retourne le dialogue actuel et passe au suivant"""
        if not self.is_alive:
            return f"{self.name} est mort et ne peut pas parler."
        dialogue = self.dialogues[self.dialogue_index]
        self.dialogue_index = (self.dialogue_index + 1) % len(self.dialogues)
        return f"{self.name} dit : {dialogue}"

    def take_damage(self, damage):
        """Inflige des dégâts au PNJ"""
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            return f"{self.name} est vaincu !"
        return f"{self.name} a {self.health} PV restants."

    def move_to_room(self, room):
        """Déplace le PNJ vers une nouvelle pièce"""
        self.current_room = room