from player import Player

def test_player_initialization():
    p = Player("John")
    assert p.money == 10000
    assert p.position == 0

def test_player_move():
    p = Player("John")
    p.move(5, 20)
    assert p.position == 5

def test_player_retirement():
    p = Player("John")
    p.move(25, 20)
    assert p.retired is True