let gameId = null;
let commandHistory = [];
let historyIndex = -1;

// Démarrer le jeu
async function startGame() {
    const playerName = document.getElementById('playerName').value;
    
    try {
        const response = await fetch('/api/start_game', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: playerName })
        });
        
        const data = await response.json();
        gameId = data.game_id;
        
        document.getElementById('startMenu').style.display = 'none';
        document.getElementById('gameScreen').style.display = 'flex';
        document.getElementById('playerNameDisplay').textContent = data.player_name;
        
        addMessage(data.message);
        updateGameStatus();
        document.getElementById('commandInput').focus();
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur au démarrage du jeu');
    }
}

// Mettre à jour le statut du jeu
async function updateGameStatus() {
    if (!gameId) return;
    
    try {
        const response = await fetch(`/api/game/${gameId}/status`);
        const data = await response.json();
        
        // Mise à jour du joueur
        document.getElementById('playerNameDisplay').textContent = data.player_name;
        updateHealthBar(data.player_health, data.player_max_health);
        
        // Mise à jour de la pièce
        document.getElementById('roomName').textContent = data.current_room;
        document.getElementById('roomDesc').textContent = data.room_description;
        
        // Sorties
        const exitsText = data.exits.length > 0 ? '🚪 ' + data.exits.join(', ') : 'Aucune sortie';
        document.getElementById('roomExits').textContent = exitsText;
        
        // Objets dans la pièce
        const itemsDiv = document.getElementById('roomItems');
        if (data.items.length > 0) {
            itemsDiv.innerHTML = '<strong>📦 Objets :</strong><br>' + data.items.map(item => `• ${item}`).join('<br>');
        } else {
            itemsDiv.innerHTML = '';
        }
        
        // PNJs dans la pièce
        const npcsDiv = document.getElementById('roomNPCs');
        if (data.npcs_in_room.length > 0) {
            npcsDiv.innerHTML = '<strong>👤 PNJs :</strong><br>' + data.npcs_in_room.map(npc => `• ${npc}`).join('<br>');
        } else {
            npcsDiv.innerHTML = '';
        }
        
        // Inventaire
        updateInventory(data.inventory);
        
        // Quêtes
        updateQuests(data.quests);
        
        // Statut actuel
        document.getElementById('currentRoomStatus').textContent = `Pièce: ${data.current_room}`;
        
        // Vérifier si le jeu est terminé
        if (data.finished) {
            setTimeout(endGame, 500);
        }
    } catch (error) {
        console.error('Erreur:', error);
    }
}

// Envoyer une commande
async function sendCommand() {
    const input = document.getElementById('commandInput');
    const command = input.value.trim();
    
    if (!command || !gameId) return;
    
    input.value = '';
    commandHistory.push(command);
    historyIndex = -1;
    
    addMessage(`> ${command}`, 'command');
    
    try {
        const response = await fetch(`/api/game/${gameId}/command`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: command })
        });
        
        const data = await response.json();
        
        if (data.message) {
            // Parser le message pour détecter les types
            const message = data.message.trim();
            if (message.includes('Quête') || message.includes('complétée')) {
                addMessage(message, 'quest');
            } else if (message.includes('erreur') || message.includes('inconnue')) {
                addMessage(message, 'error');
            } else {
                addMessage(message);
            }
        }
        
        updateGameStatus();
        
        if (data.finished) {
            setTimeout(endGame, 500);
        }
    } catch (error) {
        console.error('Erreur:', error);
        addMessage('Erreur lors de l\'exécution de la commande', 'error');
    }
    
    input.focus();
}

// Commande rapide
async function quickCommand(cmd) {
    document.getElementById('commandInput').value = cmd;
    await sendCommand();
}

// Ajouter un message
function addMessage(message, type = '') {
    const history = document.getElementById('messageHistory');
    const p = document.createElement('p');
    p.textContent = message;
    if (type) p.className = type;
    history.appendChild(p);
    history.scrollTop = history.scrollHeight;
}

// Mettre à jour la barre de santé
function updateHealthBar(current, max) {
    const percentage = (current / max) * 100;
    const fill = document.getElementById('healthFill');
    fill.style.width = percentage + '%';
    document.getElementById('healthText').textContent = `${current}/${max} HP`;
}

// Mettre à jour l'inventaire
function updateInventory(inventory) {
    const inventoryDiv = document.getElementById('inventoryContent');
    if (inventory.length === 0) {
        inventoryDiv.innerHTML = '<p class="empty">Vide</p>';
    } else {
        inventoryDiv.innerHTML = inventory.map(item => `<p>🎒 ${item}</p>`).join('');
    }
}

// Mettre à jour les quêtes
function updateQuests(quests) {
    const questsDiv = document.getElementById('questsContent');
    questsDiv.innerHTML = quests.map(quest => {
        const className = quest.completed ? 'completed' : '';
        return `<p class="${className}">${quest.status} ${quest.name}</p>`;
    }).join('');
}

// Gestion des touches
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendCommand();
    } else if (event.key === 'ArrowUp') {
        event.preventDefault();
        historyUp();
    } else if (event.key === 'ArrowDown') {
        event.preventDefault();
        historyDown();
    }
}

// Navigation historique
function historyUp() {
    if (commandHistory.length > 0) {
        historyIndex = Math.min(historyIndex + 1, commandHistory.length - 1);
        const input = document.getElementById('commandInput');
        input.value = commandHistory[commandHistory.length - 1 - historyIndex];
    }
}

function historyDown() {
    if (historyIndex > 0) {
        historyIndex--;
        const input = document.getElementById('commandInput');
        input.value = commandHistory[commandHistory.length - 1 - historyIndex];
    } else if (historyIndex === 0) {
        historyIndex = -1;
        document.getElementById('commandInput').value = '';
    }
}

// Terminer le jeu
async function endGame() {
    try {
        const response = await fetch(`/api/game/${gameId}/end`);
        const data = await response.json();
        
        document.getElementById('gameScreen').style.display = 'none';
        document.getElementById('endScreen').style.display = 'flex';
        
        const isVictory = data.result.includes('VICTOIRE');
        document.getElementById('endTitle').textContent = data.result;
        document.getElementById('endTitle').style.color = isVictory ? '#00ff00' : '#ff0000';
        
        document.getElementById('endMessage').textContent = 
            isVictory ? 
            'Félicitations ! Vous avez réussi à vous échapper du labyrinthe !' :
            'Vous avez été vaincu... Le labyrinthe reste votre prison.';
        
        gameId = null;
    } catch (error) {
        console.error('Erreur:', error);
    }
}

// Quitter le jeu
function quitGame() {
    if (confirm('Êtes-vous sûr de vouloir quitter la partie ?')) {
        document.getElementById('gameScreen').style.display = 'none';
        document.getElementById('startMenu').style.display = 'flex';
        gameId = null;
        commandHistory = [];
        historyIndex = -1;
        document.getElementById('playerName').value = 'Aventurier';
        document.getElementById('messageHistory').innerHTML = '';
    }
}

// Initialiser
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('playerName').focus();
});
