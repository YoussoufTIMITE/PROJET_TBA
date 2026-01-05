# Explication du Code du Jeu d'Aventure TBA

## Introduction

Le projet TBA est un jeu d'aventure textuel écrit en Python. Le joueur explore un labyrinthe, collecte des objets, interagit avec des personnages non-joueurs (PNJ), accomplit des quêtes et combat des ennemis pour gagner.

Le jeu est structuré en modules orientés objet, chacun responsable d'une partie spécifique du système.

## Architecture Générale

Le jeu suit une architecture modulaire avec les composants suivants :

- **game.py** : Point d'entrée et boucle principale du jeu.
- **player.py** : Gestion du joueur (position, inventaire, santé).
- **room.py** : Représentation des pièces du labyrinthe.
- **item.py** : Objets collectables.
- **npc.py** : Personnages non-joueurs.
- **quest.py** : Système de quêtes.
- **command.py** : Définition des commandes disponibles.
- **actions.py** : Implémentation des actions du joueur.
- **tests/** : Tests unitaires pour valider le code.

## Description Détaillée des Modules

### 1. game.py

Ce module contient la classe `Game`, qui gère l'initialisation, la configuration et la boucle principale.

#### Classe Game
- **Attributs** :
  - `finished` : Booléen indiquant si le jeu est terminé.
  - `rooms` : Liste des pièces du jeu.
  - `commands` : Dictionnaire des commandes disponibles.
  - `player` : Instance du joueur.
  - `ghost_defeated` : Indicateur pour la progression.
  - `quests` : Liste des quêtes.

- **Méthodes principales** :
  - `setup()` : Configure les commandes, pièces, objets, PNJ et quêtes.
  - `move_npcs()` : Déplace aléatoirement les PNJ.
  - `print_welcome()` : Affiche le message de bienvenue.
  - `process_command()` : Traite les entrées du joueur.
  - `play()` : Boucle principale du jeu.

#### Exemple d'utilisation
```python
game = Game()
game.play()
```

### 2. player.py

Gère l'état et les actions du joueur.

#### Classe Player
- **Attributs** :
  - `name` : Nom du joueur.
  - `current_room` : Pièce actuelle.
  - `history` : Historique des pièces visitées.
  - `inventory` : Liste des objets possédés.
  - `health` : Points de vie.
  - `direction_aliases` : Dictionnaire pour normaliser les directions.

- **Méthodes principales** :
  - `normalize_direction(direction)` : Convertit les alias de direction.
  - `move(direction)` : Déplace le joueur.
  - `add_item_to_inventory(item)` / `remove_item_from_inventory(item)` : Gestion de l'inventaire.
  - `take_damage(damage)` : Inflige des dégâts.

### 3. room.py

Représente les pièces du labyrinthe.

#### Classe Room
- **Attributs** :
  - `name` : Nom de la pièce.
  - `description` : Description textuelle.
  - `exits` : Dictionnaire des sorties (direction -> Room).
  - `items` : Objets présents.
  - `npcs` : PNJ présents.

- **Méthodes principales** :
  - `get_long_description()` : Description complète avec sorties, objets et PNJ.
  - `add_item(item)` / `remove_item(item)` : Gestion des objets.
  - `add_npc(npc)` / `remove_npc(npc)` : Gestion des PNJ.
  - `get_item_by_name(name)` / `get_npc_by_name(name)` : Recherche par nom.

### 4. item.py

Objets simples du jeu.

#### Classe Item
- **Attributs** :
  - `name` : Nom de l'objet.
  - `description` : Description.

### 5. npc.py

Personnages non-joueurs avec dialogues et combat.

#### Classe NPC
- **Attributs** :
  - `name` : Nom du PNJ.
  - `description` : Description.
  - `dialogues` : Liste des dialogues.
  - `dialogue_index` : Index du dialogue actuel.
  - `health` : Points de vie.
  - `is_alive` : Statut de vie.
  - `talked` : Indicateur si le joueur a parlé.

- **Méthodes principales** :
  - `talk()` : Retourne le dialogue suivant.
  - `take_damage(damage)` : Inflige des dégâts.

### 6. quest.py

Système de quêtes pour guider le joueur.

#### Classe Quest
- **Attributs** :
  - `name` : Nom de la quête.
  - `description` : Description.
  - `quest_type` : Type ('location', 'item', 'npc').
  - `target` : Cible à atteindre.
  - `completed` : Statut.
  - `reward` : Récompense.

- **Méthodes principales** :
  - `check_completion(game)` : Vérifie si la quête est accomplie.

### 7. command.py

Définition des commandes.

#### Classe Command
- **Attributs** :
  - `name` : Nom de la commande.
  - `description` : Description.
  - `action` : Fonction associée.
  - `nb_params` : Nombre de paramètres.

### 8. actions.py

Implémentation des actions du joueur.

#### Classe Actions
Contient des méthodes statiques pour chaque commande :
- `go(game, words, nb_params)` : Déplacement.
- `take(game, words, nb_params)` : Prendre un objet.
- `drop(game, words, nb_params)` : Poser un objet.
- `talk(game, words, nb_params)` : Parler à un PNJ.
- `attack(game, words, nb_params)` : Attaquer un PNJ.
- Etc.

Chaque méthode vérifie les paramètres, effectue l'action et met à jour les quêtes.

## Flux du Jeu

1. **Initialisation** : `Game.setup()` crée les pièces, objets, PNJ et quêtes.
2. **Boucle principale** : `Game.play()` affiche le bienvenue et traite les commandes.
3. **Traitement des commandes** : `process_command()` parse l'entrée et appelle l'action correspondante.
4. **Mise à jour** : Les actions déplacent les PNJ et vérifient les quêtes.

## Tests

Les tests sont dans `tests/test_actions.py` et utilisent pytest. Ils couvrent :
- Mouvements et historique.
- Prise et dépôt d'objets.
- Dialogue avec PNJ.
- Combat.

Pour exécuter : `pytest tests/`

## Comment Convertir ce Document en PDF

1. Installez un convertisseur Markdown vers PDF, comme `pandoc` :
   ```
   sudo apt install pandoc texlive-latex-base
   ```
2. Convertissez :
   ```
   pandoc CODE_EXPLANATION.md -o CODE_EXPLANATION.pdf
   ```

Ou utilisez un outil en ligne comme Markdown to PDF.

## Conclusion

Le code est modulaire, extensible et suit les principes OOP. Les améliorations récentes incluent des tests, une meilleure documentation et un nettoyage du code.