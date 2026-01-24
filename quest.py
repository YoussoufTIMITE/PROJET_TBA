class Quest:
    def __init__(self, name, description, quest_type, target, reward=None):
        self.name = name
        self.description = description
        self.quest_type = quest_type  # 'location', 'item', 'npc', 'defeat_npc'
        self.target = target  # nom de la pièce, objet ou PNJ
        self.completed = False
        self.reward = reward  # peut-être un objet ou un message

    def check_completion(self, game):
        if self.completed:
            return False
        if self.quest_type == 'location':
            if game.player.current_room.name.lower() == self.target.lower():
                self.completed = True
                print(f"\nQuête '{self.name}' complétée ! {self.reward}\n")
                return True
        elif self.quest_type == 'item':
            if any(item.name.lower() == self.target.lower() for item in game.player.inventory):
                self.completed = True
                print(f"\nQuête '{self.name}' complétée ! {self.reward}\n")
                return True
        elif self.quest_type == 'npc':
            for room in game.rooms:
                for npc in room.npcs:
                    if npc.name.lower() == self.target.lower() and npc.talked:
                        self.completed = True
                        print(f"\nQuête '{self.name}' complétée ! {self.reward}\n")
                        return True
        elif self.quest_type == 'defeat_npc':
            # Cherche si le PNJ est mort en cherchant dans tous les rooms
            for room in game.rooms:
                for npc in room.npcs:
                    if npc.name.lower() == self.target.lower() and not npc.is_alive:
                        self.completed = True
                        print(f"\nQuête '{self.name}' complétée ! {self.reward}\n")
                        return True
        return False
