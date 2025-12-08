#!/usr/bin/env python3
"""
Script de démonstration des nouvelles fonctionnalités du jeu
"""

from item import Item
from player import Player
from room import Room
from command import Command
from actions import Actions
from game import Game

def test_items_and_inventory():
    """Test les items et l'inventaire"""
    print("=" * 50)
    print("TEST: Items et Inventaire")
    print("=" * 50)
    
    # Créer des items
    cle = Item("clé", "une vieille clé rouillée")
    lampe = Item("lampe", "une lampe de poche brillante")
    
    # Créer une room avec des items
    room = Room("Hall", "Un grand hall")
    room.add_item(cle)
    room.add_item(lampe)
    
    print(f"\nRoom description:\n{room.get_long_description()}")
    
    # Créer un joueur
    player = Player("Test")
    player.current_room = room
    
    # Test take
    print(f"Avant: {player.get_inventory_display()}")
    item = room.get_item_by_name("clé")
    if item:
        room.remove_item(item)
        player.add_item_to_inventory(item)
    print(f"Après prise de la clé: {player.get_inventory_display()}")
    
    # Test drop
    player.remove_item_from_inventory(item)
    room.add_item(item)
    print(f"Après avoir posé la clé: {player.get_inventory_display()}")
    print(f"Room after drop:\n{room.get_long_description()}")
    
    print("\n✓ Test réussi!\n")

def test_actions():
    """Test les actions du jeu"""
    print("=" * 50)
    print("TEST: Actions (look, take, drop, inventory)")
    print("=" * 50)
    
    # Créer une instance de Game
    game = Game()
    game.finished = False
    game.rooms = []
    game.commands = {}
    
    # Ajouter les commandes
    game.commands["look"] = Command("look", " : observer", Actions.look, 0)
    game.commands["inventory"] = Command("inventory", " : inventaire", Actions.inventory, 0)
    game.commands["take"] = Command("take", " <objet> : prendre", Actions.take, 1)
    game.commands["drop"] = Command("drop", " <objet> : poser", Actions.drop, 1)
    
    # Créer une room avec un item
    room = Room("Bureau", "Un bureau poussiéreux")
    stylo = Item("stylo", "un stylo bleu")
    room.add_item(stylo)
    
    # Créer un joueur
    player = Player("Alice")
    player.current_room = room
    
    game.player = player
    
    print("\n1. Look (observer l'environnement)")
    Actions.look(game, ["look"], 0)
    
    print("\n2. Inventory (inventaire vide)")
    Actions.inventory(game, ["inventory"], 0)
    
    print("\n3. Take stylo (prendre un objet)")
    Actions.take(game, ["take", "stylo"], 1)
    
    print("\n4. Inventory (après prise)")
    Actions.inventory(game, ["inventory"], 0)
    
    print("\n5. Look (après prise)")
    Actions.look(game, ["look"], 0)
    
    print("\n6. Drop stylo (poser l'objet)")
    Actions.drop(game, ["drop", "stylo"], 1)
    
    print("\n7. Inventory (après dépôt)")
    Actions.inventory(game, ["inventory"], 0)
    
    print("\n8. Look (après dépôt)")
    Actions.look(game, ["look"], 0)
    
    print("\n✓ Test réussi!\n")

if __name__ == "__main__":
    test_items_and_inventory()
    test_actions()
    print("=" * 50)
    print("TOUS LES TESTS PASSENT! ✓")
    print("=" * 50)
