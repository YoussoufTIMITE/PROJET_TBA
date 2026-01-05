# TBA

Ce repo contient le jeu d’aventure TBA, un jeu textuel où le joueur explore un labyrinthe, collecte des objets, interagit avec des PNJ et accomplit des quêtes pour gagner.

Le jeu comprend plusieurs pièces interconnectées, des objets à ramasser, des personnages non-joueurs (PNJ) avec lesquels parler ou combattre, et un système de quêtes. Le but est de vaincre le Fantôme puis le Gardien pour s'échapper.

## Structuration

Le projet est organisé en plusieurs modules :

- `game.py` / `Game` : classe principale gérant l'environnement, la configuration du jeu et la boucle principale ;
- `room.py` / `Room` : propriétés d'un lieu (nom, description, sorties, objets, PNJ) ;
- `player.py` / `Player` : le joueur (position, inventaire, historique, santé) ;
- `command.py` / `Command` : les commandes disponibles (nom, description, action associée) ;
- `actions.py` / `Actions` : les interactions et actions du joueur (se déplacer, prendre des objets, parler, combattre, etc.) ;
- `item.py` / `Item` : les objets du jeu (nom, description) ;
- `npc.py` / `NPC` : les personnages non-joueurs (nom, description, dialogues, santé) ;
- `quest.py` / `Quest` : les quêtes (nom, description, conditions, récompenses).

## Comment jouer

Lancez le jeu avec `python game.py`. Entrez des commandes comme `go N`, `take clé`, `talk Marchand`, `attack Fantome`, etc. Tapez `help` pour la liste des commandes.

## Tests

Les tests sont dans le dossier `tests/`. Lancez-les avec `pytest`.
