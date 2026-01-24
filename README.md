# Jeu d’aventure – TBA

Ce dépôt contient le jeu d’aventure **TBA**, un jeu textuel dans lequel le joueur explore un labyrinthe, collecte des objets, interagit avec des personnages non-joueurs (PNJ) et accomplit des quêtes afin de s’échapper.

L’objectif principal est de progresser à travers différentes pièces, vaincre le **Fantôme**, puis le **Gardien**, pour gagner la partie.

## Description de la version actuelle

Cette version comprend les éléments suivants :

- Une structure modulaire avec plusieurs classes et fichiers interconnectés.
- Un gameplay basé sur des commandes textuelles simples.
- Un labyrinthe composé de plusieurs pièces interconnectées.
- Des objets à ramasser et utiliser.
- Des PNJ avec lesquels le joueur peut dialoguer ou combattre.
- Un système de quêtes permettant de guider la progression du joueur.

## Fonctionnalités actuelles

- Navigation entre plusieurs pièces.
- Gestion de l’inventaire du joueur.
- Interaction avec des objets (ramassage).
- Dialogues et combats avec des personnages non-joueurs.
- Système de quêtes avec conditions et récompenses.
- Commandes textuelles pour interagir avec l’environnement (`go`, `take`, `talk`, `attack`, etc.).

## Limites

- Interface exclusivement textuelle.
- Comportements des PNJ encore simples.
- Interactions limitées à des actions prédéfinies.
- Absence d’éléments graphiques et sonores.

## Structuration du projet

La base de code est organisée en plusieurs modules, chacun correspondant à une classe centrale du jeu :

- `game.py` / `Game` : gestion de l’environnement du jeu, configuration et boucle principale ;
- `room.py` / `Room` : représentation des lieux (nom, description, sorties, objets, PNJ) ;
- `player.py` / `Player` : gestion du joueur (position, inventaire, santé, historique) ;
- `command.py` / `Command` : définition et exécution des commandes ;
- `actions.py` / `Actions` : gestion des interactions (déplacement, prise d’objets, dialogues, combats, etc.) ;
- `item.py` / `Item` : représentation des objets du jeu ;
- `character.py` / `NPC` : gestion des personnages non-joueurs (dialogues, santé) ;
- `quest.py` / `Quest` : gestion des quêtes (objectifs, conditions, récompenses).

## Comment jouer

Lancez le jeu avec la commande suivante :

```bash
python game.py

-À venir

Ajout d’objets interactifs et d’événements dynamiques. -Implémentation d’une intelligence artificielle basique pour les PNJ. Amélioration des graphismes et de l’interface utilisateur. -Développement de scénarios immersifs et personnalisés.

Merci de votre intérêt pour ce projet ! Toutes les suggestions ou contributions sont les bienvenues. 😊
