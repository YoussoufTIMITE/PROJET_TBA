import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from tkinter import font as tkFont
from game import Game
import threading

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu d'aventure - TBA")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a1a")
        
        self.game = None
        self.game_started = False
        self.command_history = []
        self.history_index = -1
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        """Configure les styles Tkinter"""
        self.bg_color = "#1a1a1a"
        self.fg_color = "#ffffff"
        self.accent_color = "#00d4ff"
        self.button_color = "#2a2a2a"
        
        self.title_font = tkFont.Font(family="Arial", size=14, weight="bold")
        self.text_font = tkFont.Font(family="Courier", size=10)
        self.button_font = tkFont.Font(family="Arial", size=9)
        
    def create_widgets(self):
        """Crée tous les widgets de l'interface"""
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # === HAUT : Titre et statut ===
        header_frame = tk.Frame(main_frame, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title_label = tk.Label(header_frame, text="⚔️ JEU D'AVENTURE - TBA ⚔️", 
                              font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        title_label.pack(side=tk.LEFT)
        
        # === GAUCHE : Pièce + Inventaire + Quêtes ===
        left_frame = tk.Frame(main_frame, bg=self.bg_color)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Section Pièce actuelle
        room_label = tk.Label(left_frame, text="📍 PIÈCE ACTUELLE", 
                             font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        room_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.room_text = scrolledtext.ScrolledText(left_frame, height=8, bg="#2a2a2a", 
                                                   fg=self.fg_color, font=self.text_font)
        self.room_text.pack(fill=tk.BOTH, expand=False, pady=(0, 10))
        
        # Section Inventaire
        inv_label = tk.Label(left_frame, text="🎒 INVENTAIRE", 
                            font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        inv_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.inventory_text = scrolledtext.ScrolledText(left_frame, height=6, bg="#2a2a2a", 
                                                        fg=self.fg_color, font=self.text_font)
        self.inventory_text.pack(fill=tk.BOTH, expand=False, pady=(0, 10))
        
        # Section Quêtes
        quest_label = tk.Label(left_frame, text="📋 QUÊTES", 
                              font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        quest_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.quest_text = scrolledtext.ScrolledText(left_frame, height=6, bg="#2a2a2a", 
                                                    fg=self.fg_color, font=self.text_font)
        self.quest_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # === DROITE : Historique + Commandes ===
        right_frame = tk.Frame(main_frame, bg=self.bg_color, width=350)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        right_frame.pack_propagate(False)
        
        # Section Statut
        status_label = tk.Label(right_frame, text="❤️ STATUT", 
                               font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        status_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.status_text = tk.Label(right_frame, text="En attente...", 
                                    font=self.text_font, bg="#2a2a2a", fg=self.fg_color,
                                    justify=tk.LEFT, wraplength=300)
        self.status_text.pack(fill=tk.X, pady=(0, 10), padx=5)
        
        # Section Historique
        history_label = tk.Label(right_frame, text="📜 HISTORIQUE", 
                                font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        history_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.message_text = scrolledtext.ScrolledText(right_frame, height=20, bg="#2a2a2a", 
                                                      fg=self.fg_color, font=self.text_font)
        self.message_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Section Commandes
        cmd_label = tk.Label(right_frame, text="⌨️ COMMANDE", 
                            font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        cmd_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Frame pour l'input
        input_frame = tk.Frame(right_frame, bg=self.bg_color)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.command_input = tk.Entry(input_frame, bg="#2a2a2a", fg=self.fg_color, 
                                      font=self.text_font, insertbackground=self.accent_color)
        self.command_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.command_input.bind("<Return>", lambda e: self.execute_command())
        self.command_input.bind("<Up>", self.history_up)
        self.command_input.bind("<Down>", self.history_down)
        
        send_btn = tk.Button(input_frame, text="▶ ENVOYER", bg=self.button_color, 
                            fg=self.accent_color, font=self.button_font, 
                            command=self.execute_command, activebackground=self.accent_color,
                            activeforeground=self.bg_color)
        send_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # === BOUTONS RAPIDES ===
        buttons_label = tk.Label(right_frame, text="🎮 ACTIONS RAPIDES", 
                                font=self.title_font, bg=self.bg_color, fg=self.accent_color)
        buttons_label.pack(anchor=tk.W, pady=(0, 5))
        
        buttons_frame = tk.Frame(right_frame, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 10))
        
        quick_commands = [
            ("Aide", "help"),
            ("Inventaire", "inventory"),
            ("État", "status"),
            ("Quêtes", "quests"),
            ("PNJ", "listPNJ"),
            ("Attendre", "wait"),
        ]
        
        for text, cmd in quick_commands:
            btn = tk.Button(buttons_frame, text=text, bg=self.button_color, 
                           fg=self.accent_color, font=self.button_font,
                           command=lambda c=cmd: self.quick_command(c),
                           activebackground=self.accent_color, activeforeground=self.bg_color)
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # === BOUTONS BAS ===
        bottom_frame = tk.Frame(main_frame, bg=self.bg_color)
        bottom_frame.pack(fill=tk.X, pady=(10, 0))
        
        start_btn = tk.Button(bottom_frame, text="🎮 NOUVELLE PARTIE", bg="#00aa00", 
                             fg=self.fg_color, font=self.button_font, 
                             command=self.start_game, activebackground="#00dd00")
        start_btn.pack(side=tk.LEFT, padx=5)
        
        quit_btn = tk.Button(bottom_frame, text="❌ QUITTER", bg="#aa0000", 
                            fg=self.fg_color, font=self.button_font,
                            command=self.root.quit, activebackground="#dd0000")
        quit_btn.pack(side=tk.LEFT, padx=5)
        
    def start_game(self):
        """Démarre une nouvelle partie"""
        if self.game_started:
            messagebox.showwarning("Attention", "Une partie est déjà en cours!")
            return
        
        # Créer une nouvelle partie
        self.game = Game()
        self.game_started = True
        
        # Demander le nom du joueur
        dialog = tk.Toplevel(self.root)
        dialog.title("Nouveau Joueur")
        dialog.geometry("300x100")
        dialog.configure(bg=self.bg_color)
        
        tk.Label(dialog, text="Entrez votre nom :", bg=self.bg_color, 
                fg=self.fg_color, font=self.text_font).pack(pady=10)
        
        name_entry = tk.Entry(dialog, bg="#2a2a2a", fg=self.fg_color, font=self.text_font)
        name_entry.pack(padx=20, fill=tk.X)
        name_entry.focus()
        
        def confirm_name():
            name = name_entry.get().strip() or "Aventurier"
            dialog.destroy()
            self.init_game(name)
        
        tk.Button(dialog, text="OK", bg=self.button_color, fg=self.accent_color,
                 command=confirm_name).pack(pady=10)
        
    def init_game(self, name):
        """Initialise le jeu avec le nom du joueur"""
        self.game.setup()
        self.game.player.name = name
        self.game.player.current_room = list(self.game.rooms)[0]
        self.game.player.history = [self.game.player.current_room]
        
        self.add_message(f"Bienvenue {name} dans cette aventure mystérieuse !")
        self.add_message("Vous êtes piégé dans un labyrinthe. Parlez au Marchand pour des indices.")
        self.add_message("Vainquez d'abord le Fantôme, puis le Gardien pour gagner !")
        
        self.command_input.focus()
        self.update_display()
        
    def update_display(self):
        """Met à jour l'affichage du jeu"""
        if not self.game or not self.game_started:
            return
        
        # Mise à jour de la pièce
        self.room_text.config(state=tk.NORMAL)
        self.room_text.delete(1.0, tk.END)
        self.room_text.insert(tk.END, self.game.player.current_room.get_long_description())
        self.room_text.config(state=tk.DISABLED)
        
        # Mise à jour de l'inventaire
        self.inventory_text.config(state=tk.NORMAL)
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.insert(tk.END, self.game.player.get_inventory_display())
        self.inventory_text.config(state=tk.DISABLED)
        
        # Mise à jour du statut
        status = f"Joueur: {self.game.player.name}\nHP: {self.game.player.health}/100\nPièce: {self.game.player.current_room.name}"
        self.status_text.config(text=status)
        
        # Mise à jour des quêtes
        self.quest_text.config(state=tk.NORMAL)
        self.quest_text.delete(1.0, tk.END)
        for quest in self.game.quests:
            status = "✓" if quest.completed else "○"
            self.quest_text.insert(tk.END, f"{status} {quest.name}\n")
        self.quest_text.config(state=tk.DISABLED)
        
    def execute_command(self):
        """Exécute une commande"""
        if not self.game or not self.game_started:
            messagebox.showwarning("Attention", "Commencez une partie d'abord!")
            return
        
        command = self.command_input.get().strip()
        if not command:
            return
        
        self.command_input.delete(0, tk.END)
        self.command_history.append(command)
        self.history_index = -1
        
        self.add_message(f"> {command}")
        
        # Capture la sortie et la redirige vers le message
        import io
        import sys
        
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        try:
            self.game.process_command(command)
        finally:
            output = buffer.getvalue()
            sys.stdout = old_stdout
        
        if output:
            self.add_message(output)
        
        self.update_display()
        
        # Vérifier si le jeu est terminé
        if self.game.finished:
            self.game_ended()
        
    def quick_command(self, cmd):
        """Exécute une commande rapide"""
        self.command_input.delete(0, tk.END)
        self.command_input.insert(0, cmd)
        self.execute_command()
        
    def add_message(self, message):
        """Ajoute un message à l'historique"""
        self.message_text.config(state=tk.NORMAL)
        self.message_text.insert(tk.END, message + "\n")
        self.message_text.see(tk.END)
        self.message_text.config(state=tk.DISABLED)
        
    def history_up(self, event=None):
        """Navigation dans l'historique (haut)"""
        if self.command_history:
            self.history_index = min(self.history_index + 1, len(self.command_history) - 1)
            self.command_input.delete(0, tk.END)
            self.command_input.insert(0, self.command_history[-(self.history_index + 1)])
        return "break"
        
    def history_down(self, event=None):
        """Navigation dans l'historique (bas)"""
        if self.history_index > 0:
            self.history_index -= 1
            self.command_input.delete(0, tk.END)
            self.command_input.insert(0, self.command_history[-(self.history_index + 1)])
        elif self.history_index == 0:
            self.history_index = -1
            self.command_input.delete(0, tk.END)
        return "break"
        
    def game_ended(self):
        """Appelé quand le jeu se termine"""
        if self.game.player.health <= 0:
            messagebox.showinfo("GAME OVER", "Vous avez été vaincu !\nFin de la partie.")
        else:
            messagebox.showinfo("VICTOIRE", "Vous avez gagné !\nFélicitations !")
        
        self.game_started = False
        self.command_input.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    gui = GameGUI(root)
    root.mainloop()
