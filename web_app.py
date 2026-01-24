from flask import Flask, render_template, request, jsonify, session
from game import Game
import os
import secrets

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = secrets.token_hex(16)

# Stocker les parties en cours
games = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/start_game', methods=['POST'])
def start_game():
    """Démarre une nouvelle partie"""
    data = request.json
    player_name = data.get('name', 'Aventurier').strip() or 'Aventurier'
    
    game = Game()
    game.setup()
    game.player.name = player_name
    
    game_id = secrets.token_hex(8)
    games[game_id] = game
    
    return jsonify({
        'game_id': game_id,
        'player_name': game.player.name,
        'message': f'Bienvenue {game.player.name} dans cette aventure mystérieuse !\nVous êtes piégé dans un labyrinthe. Parlez au Marchand pour des indices.\nVainquez d\'abord le Fantôme, puis le Gardien pour gagner !'
    })

@app.route('/api/game/<game_id>/status')
def game_status(game_id):
    """Récupère l'état actuel du jeu"""
    if game_id not in games:
        return jsonify({'error': 'Partie non trouvée'}), 404
    
    game = games[game_id]
    
    # Préparer les quêtes
    quests = []
    for quest in game.quests:
        quests.append({
            'name': quest.name,
            'description': quest.description,
            'completed': quest.completed,
            'status': '✓' if quest.completed else '○'
        })
    
    # Préparer l'inventaire
    inventory = [item.name for item in game.player.inventory]
    
    # Préparer les PNJs
    npcs = []
    for room in game.rooms:
        for npc in room.npcs:
            if npc.is_alive:
                npcs.append({
                    'name': npc.name,
                    'room': room.name,
                    'health': npc.health
                })
    
    return jsonify({
        'player_name': game.player.name,
        'player_health': game.player.health,
        'player_max_health': 100,
        'current_room': game.player.current_room.name,
        'room_description': game.player.current_room.description,
        'exits': list(game.player.current_room.exits.keys()),
        'items': [item.name for item in game.player.current_room.items],
        'npcs_in_room': [npc.name for npc in game.player.current_room.npcs if npc.is_alive],
        'inventory': inventory,
        'quests': quests,
        'npcs': npcs,
        'finished': game.finished,
        'ghost_defeated': game.ghost_defeated
    })

@app.route('/api/game/<game_id>/command', methods=['POST'])
def execute_command(game_id):
    """Exécute une commande dans le jeu"""
    if game_id not in games:
        return jsonify({'error': 'Partie non trouvée'}), 404
    
    game = games[game_id]
    data = request.json
    command = data.get('command', '').strip()
    
    if not command:
        return jsonify({'message': ''})
    
    # Capture la sortie
    import io
    import sys
    
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    try:
        game.process_command(command)
    finally:
        output = buffer.getvalue()
        sys.stdout = old_stdout
    
    return jsonify({
        'message': output,
        'finished': game.finished
    })

@app.route('/api/game/<game_id>/end')
def end_game(game_id):
    """Termine une partie"""
    if game_id in games:
        game = games[game_id]
        if game.player.health <= 0:
            result = "GAME OVER - Vous avez été vaincu !"
        else:
            result = "VICTOIRE - Vous avez gagné !"
        del games[game_id]
        return jsonify({'result': result})
    return jsonify({'error': 'Partie non trouvée'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
