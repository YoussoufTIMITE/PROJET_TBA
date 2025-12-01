import pytest

from player import Player
from room import Room
from actions import Actions


class DummyGame:
    def __init__(self, player):
        self.player = player
        self.commands = {}


def test_move_and_history_and_get_history():
    entree = Room("Entrée", "desc")
    hall = Room("Hall", "desc")
    entree.exits = {"N": hall}

    p = Player("Test")
    p.current_room = entree
    p.history.append(entree)

    assert p.move("N") is True
    assert p.current_room is hall
    assert len(p.history) == 2
    assert "Entrée" in p.get_history()

    game = DummyGame(p)
    # historik should return True and print history
    assert Actions.historik(game, ["historik"], 0) is True


def test_back_action():
    entree = Room("Entrée", "desc")
    hall = Room("Hall", "desc")
    bureau = Room("Bureau", "desc")
    entree.exits = {"N": hall}
    hall.exits = {"E": bureau}

    p = Player("Test2")
    p.current_room = entree
    p.history.append(entree)

    assert p.move("N") is True
    assert p.move("E") is True
    assert p.current_room is bureau

    game = DummyGame(p)
    assert Actions.back(game, ["back"], 0) is True
    assert p.current_room is hall


def test_back_no_previous():
    entree = Room("Entrée", "desc")
    p = Player("Solo")
    p.current_room = entree
    p.history.append(entree)
    game = DummyGame(p)
    # back should fail because there's no previous room
    assert Actions.back(game, ["back"], 0) is False
