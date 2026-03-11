from board import Board
from player import Player

def test_board_initialization():
    board = Board()
    assert board.size == 20

def test_check_space_no_special():
    board = Board()
    player = Player("John")
    result = board.check_space(player)
    assert result == "Nothing happened."