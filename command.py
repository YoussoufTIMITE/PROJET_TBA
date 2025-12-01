# command.py

class Command:
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self):
        return self.command_word + self.help_string

    # Ajout de cette méthode
    def execute(self, game, list_of_words):
        return self.action(game, list_of_words, self.number_of_parameters)