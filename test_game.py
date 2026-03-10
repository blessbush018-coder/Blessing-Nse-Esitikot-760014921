from game import Game

def test_game_initialization():
    game = Game()
    assert game.game_over is False