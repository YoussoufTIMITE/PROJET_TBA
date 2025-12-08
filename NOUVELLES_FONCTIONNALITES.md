# Nouvelles Fonctionnalités Ajoutées

## 📋 Résumé des Changements

Ce document décrit les nouvelles fonctionnalités ajoutées au jeu TBA.

---

## 1. **Classe Item** (`item.py`)

Une nouvelle classe pour représenter les objets du jeu.

### Attributs:
- `name`: Le nom de l'objet
- `description`: La description détaillée

### Méthodes:
- `__str__()`: Retourne le nom de l'objet
- `get_description()`: Retourne le nom et la description

### Exemple:
```python
cle = Item("clé", "une vieille clé rouillée")
print(cle)  # Output: clé
print(cle.get_description())  # Output: clé: une vieille clé rouillée
```

---

## 2. **Inventaire du Joueur** (`player.py`)

Ajout d'un inventaire au joueur avec les méthodes suivantes:

### Attribut:
- `inventory`: Liste des objets que le joueur possède

### Méthodes:
- `add_item_to_inventory(item)`: Ajoute un objet à l'inventaire
- `remove_item_from_inventory(item)`: Retire un objet de l'inventaire
- `get_item_from_inventory(name)`: Récupère un objet par son nom
- `get_inventory_display()`: Retourne une chaîne affichant l'inventaire

### Exemple:
```python
player = Player("Alice")
player.add_item_to_inventory(cle)
print(player.get_inventory_display())  
# Output: Inventaire : clé
```

---

## 3. **Inventaire des Lieux** (`room.py`)

Ajout d'un inventaire aux pièces avec les méthodes suivantes:

### Attribut:
- `items`: Liste des objets présents dans la pièce

### Méthodes:
- `add_item(item)`: Ajoute un objet à la pièce
- `remove_item(item)`: Retire un objet de la pièce
- `get_item_by_name(name)`: Récupère un objet par son nom

### Améliorations:
- `get_long_description()`: Affiche maintenant aussi les objets visibles dans la pièce

### Exemple:
```python
room = Room("Bureau", "Un bureau poussiéreux")
room.add_item(cle)
print(room.get_long_description())
# Affiche la description + "Objets visibles : clé"
```

---

## 4. **Nouvelles Actions** (`actions.py`)

### 🔍 **look** (observer l'environnement)
Affiche la description complète de la pièce actuelle (exits + objets visibles).

```
> look
Bureau
dans un bureau poussiéreux rempli de vieux dossiers.
Sorties disponibles : O, D
Objets visibles : livre
```

### 📦 **take** (prendre un objet)
Permet de prendre un objet dans la pièce et l'ajoute à l'inventaire.

```
> take livre
Vous avez pris : livre
```

### 🚪 **drop** (poser un objet)
Permet de poser un objet de l'inventaire dans la pièce actuelle.

```
> drop livre
Vous avez posé : livre
```

### 🎒 **inventory** (vérifier son inventaire)
Affiche la liste de tous les objets dans l'inventaire du joueur.

```
> inventory
Inventaire : clé, lampe, livre
```

---

## 5. **Objets du Jeu** (`game.py`)

Six objets ont été distribués dans les différentes pièces:

| Objet | Localisation | Description |
|-------|--------------|-------------|
| clé | Entrée | une vieille clé rouillée |
| lampe | Hall | une lampe de poche |
| livre | Bureau | un vieux livre poussiéreux |
| torche | Mezzanine | une torche éteinte |
| corde | Souterrain | une corde solide |
| pioche | Cave | une pioche usée |

---

## 6. **Liste Complète des Commandes**

| Commande | Paramètre | Description |
|----------|-----------|-------------|
| `help` | - | Afficher l'aide |
| `quit` | - | Quitter le jeu |
| `go` | `<direction>` | Se déplacer (N, S, E, O, U, D) |
| `historik` | - | Afficher l'historique des pièces visitées |
| `back` | - | Revenir à la pièce précédente |
| `look` | - | Observer l'environnement |
| `take` | `<objet>` | Prendre un objet |
| `drop` | `<objet>` | Poser un objet |
| `inventory` | - | Vérifier son inventaire |

---

## 7. **Exemple de Jeu**

```
Entrez votre nom: Alice

Bienvenue Alice dans votre univers !
Entrez 'help' si vous avez besoin d'aide.

Entrée
à l'entrée de votre univers. Une lourde porte se referme derrière vous.
Sorties disponibles : N
Objets visibles : clé

> look

Entrée
à l'entrée de votre univers. Une lourde porte se referme derrière vous.
Sorties disponibles : N
Objets visibles : clé

> take clé
Vous avez pris : clé

> inventory
Inventaire : clé

> go N

Vous vous déplacez vers N...

Hall
dans un grand hall froid et silencieux.
Sorties disponibles : S, E, U, O
Objets visibles : lampe

> take lampe
Vous avez pris : lampe

> inventory
Inventaire : clé, lampe
```

---

## 8. **Tests**

Un script de démonstration `test_demo.py` a été créé pour tester toutes les nouvelles fonctionnalités:

```bash
python test_demo.py
```

Ce script teste:
- La création d'items
- L'inventaire du joueur
- L'inventaire des pièces
- Les actions take, drop, look, inventory

