# Jeu d'aventure – TBA

Ce dépôt contient le jeu d'aventure **TBA**, un jeu textuel dans lequel le joueur explore un labyrinthe, collecte des objets, interagit avec des personnages non-joueurs (PNJ) et accomplit des quêtes afin de s'échapper.

**L'objectif principal :** Progresser à travers le labyrinthe, vaincre le **Fantôme** (premier boss), puis le **Gardien** (boss final) pour gagner la partie.

## 🎮 Description de la version actuelle

Ce jeu contient :

- ✅ Un gameplay basé sur des commandes textuelles
- ✅ Un labyrinthe composé de 8 pièces interconnectées
- ✅ 6 objets à ramasser et utiliser
- ✅ 3 PNJ (Marchand, Fantôme, Gardien) avec dialogues et combats
- ✅ Un système de 5 quêtes complètes guidant la progression
- ✅ Dégâts aléatoires en combat pour plus de défi
- ✅ Un système de points de vie (100 HP max)
- ✅ Historique de navigation

## 🎯 Fonctionnalités actuelles

### Navigation & Exploration
- Navigation entre 8 pièces (Entrée, Hall, Bureau, Mezzanine, Souterrain, Cave, Labyrinthe, Chambre du gardien)
- Système d'historique pour tracer le chemin parcouru
- Commande `back` pour revenir à la pièce précédente
- Commande `look` pour observer l'environnement

### Gestion de l'inventaire
- Ramassage et dépôt d'objets
- 6 objets avec des effets spécifiques :
  - **Clé** : Déverrouille des indices
  - **Lampe** : Révèle des informations sur les boss
  - **Livre** : Explique l'ordre de combat
  - **Torche** : Soigne le joueur (+5 HP)
  - **Corde** : Affiche la position des PNJs
  - **Pioche** : Révèle une info cruciale

### Système de PNJs
- **Marchand (Hall)** : PNJ de guide, immobile, indestructible (500 HP)
- **Fantôme (Souterrain)** : Premier boss, 30 HP, se déplace aléatoirement
- **Gardien (Chambre du gardien)** : Boss final, 100 HP, immobile

### Système de combat
- Dégâts aléatoires (15-25 pour le joueur, 10-20 pour les PNJ)
- Contre-attaque des PNJ
- **Logique d'ordre :** Le Fantôme doit être vaincu EN PREMIER
  - Si vous attaquez le Gardien avant : il se régénère
  - Si vous attaquez le Gardien après : victoire finale

### Système de quêtes (5 au total)
1. **Parler au Marchand** - Type: `npc` → Complétée au premier dialogue
2. **Collecter la Clé** - Type: `item` → Complétée au ramassage
3. **Explorer le Bureau** - Type: `location` → Complétée à l'arrivée
4. **Vaincre le Fantôme** - Type: `defeat_npc` → Complétée à la victoire
5. **Vaincre le Gardien** - Type: `defeat_npc` → Complétée à la victoire

### Commandes disponibles
```
help          - Afficher cette aide
quit          - Quitter le jeu
go <dir>      - Se déplacer (N/S/E/O/U/D)
look          - Observer l'environnement
take <objet>  - Prendre un objet
drop <objet>  - Poser un objet
inventory     - Vérifier son inventaire
status        - Vérifier votre santé
talk <pnj>    - Parler à un PNJ
attack <pnj>  - Attaquer un PNJ
wait          - Attendre (déplace les PNJs)
use <objet>   - Utiliser un objet
listPNJ       - Lister tous les PNJs vivants
historique    - Voir les pièces visitées
quests        - Afficher les quêtes
back          - Revenir à la pièce précédente
```

## 📁 Structuration du projet

La base de code est organisée en plusieurs modules :

- **`game.py`** : Gestion du jeu, configuration, boucle principale, déplacement des PNJ
- **`room.py`** : Représentation des pièces (sorties, objets, PNJ)
- **`player.py`** : Gestion du joueur (position, inventaire, santé, historique)
- **`command.py`** : Définition et exécution des commandes
- **`actions.py`** : Gestion de toutes les interactions (déplacement, combats, etc.)
- **`item.py`** : Représentation des objets
- **`character.py`** : Gestion des PNJ (dialogues, santé, déplacements)
- **`quest.py`** : Gestion des quêtes (4 types : location, item, npc, defeat_npc)

### Démarrage
```bash
python game.py
```

### Progression type
1. **Démarrez** à l'Entrée
2. **Allez au Hall** et parlez au Marchand (quête 1)
3. **Ramassez la Clé** à l'Entrée (quête 2)
4. **Explorez le Bureau** (quête 3)
5. **Allez au Souterrain** et battez le Fantôme (quête 4)
6. **Allez à la Chambre du Gardien** et battez le Gardien (quête 5 + VICTOIRE)

### Objets utiles
- Utilisez la **Torche** si votre santé baisse
- Utilisez la **Corde** pour localiser les PNJs
- Lisez le **Livre** pour les indices

## 📊 Logique du jeu

### Système de victoire
- **Condition 1 :** Vous devez vaincre le Fantôme EN PREMIER
- **Condition 2 :** Puis vaincre le Gardien
- **Résultat :** "VICTOIRE - Vous avez gagné !"

### Système de défaite
- Si votre santé ≤ 0 : "GAME OVER - Vous avez été vaincu !"

### Déplacement des PNJs
- Les PNJs (sauf Marchand et Gardien) ont 20% de chance de se déplacer par tour
- Ils ne se déplacent qu'entre les pièces avec des sorties valides
- Ils ne se déplacent pas dans la pièce du joueur

## 🔧 Améliorations récentes

- ✅ Correction complète de la logique du jeu
- ✅ Ajout de quêtes de défaite (defeat_npc)
- ✅ Protection du Marchand (santé 500, immobile)
- ✅ Dégâts aléatoires pour plus de défi
- ✅ Vérifications cohérentes de mort du joueur
- ✅ Système de fin de partie clair (VICTOIRE/GAME OVER)

## 📝 Limitations actuelles

- Interface exclusivement textuelle
- Pas d'éléments sonores
- Comportements des PNJs basiques mais fonctionnels

## 🚀 Améliorations futures

- Ajout de nouveaux types de quêtes
- Implémentation d'une intelligence artificielle plus avancée pour les PNJ
- Interface graphique (pygame, tkinter, etc.)
- Système de sauvegarde/chargement
- Niveaux de difficulté
- Plus de zones à explorer
- Système de magie/compétences

## 📄 Licence

Ce projet est open-source. Toutes les suggestions ou contributions sont les bienvenues ! 😊
