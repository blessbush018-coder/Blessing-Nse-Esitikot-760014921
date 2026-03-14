"""
Game of Life - Command Line Version
===================================

This module implements a simplified command-line version of the Game of Life.
It contains all core classes: Player, Board, Dice, Card, and Game.
"""

import random
from typing import List


class Player:
    """Represents a player in the Game of Life."""

    def __init__(self, name: str):
        """
        Initialize a player.

        Args:
            name (str): Player's name.
        """
        self.name = name
        self.money = 10000
        self.career = None
        self.house = None
        self.position = 0
        self.retired = False

    def move(self, steps: int, board_size: int = 25):
        """Move the player forward by `steps` spaces."""
        self.position = (self.position + steps) % board_size

    def summary(self):
        """Return a summary of player's status."""
        return {
            "name": self.name,
            "money": self.money,
            "career": self.career,
            "house": self.house,
            "position": self.position
        }


class Board:
    """Represents the game board."""

    def __init__(self, size: int = 20):
        """
        Initialize the board.

        Args:
            size (int): Number of spaces on the board.
        """
        self.spaces = list(range(size))

    def move_player(self, player: Player, steps: int):
        """Move player and handle board actions."""
        player.move(steps)
        if player.position >= len(self.spaces):
            player.position = len(self.spaces) - 1  # prevent overflow

    def trigger_space(self, player: Player):
        """Trigger actions for special board spaces."""
        # Example: gain money every 5th space
        if player.position % 5 == 0 and player.position != 0:
            player.money += 1000


class Dice:
    """Represents a dice."""

    @staticmethod
    def roll() -> int:
        """Roll the dice and return a number between 1 and 6."""
        return random.randint(1, 6)


class Card:
    """Represents cards in the game."""

    def __init__(self, card_type: str, value: int):
        """
        Initialize a card.

        Args:
            card_type (str): Type of card ('career', 'salary', 'action').
            value (int): Value associated with the card.
        """
        self.card_type = card_type
        self.value = value

    def apply(self, player: Player):
        """Apply card effect to a player."""
        if self.card_type == "salary":
            player.money += self.value
        elif self.card_type == "action":
            player.money += self.value  # simplified effect


class Game:
    """Controls the game loop."""

    def __init__(self):
        """Initialize the game."""
        self.players: List[Player] = []
        self.board = Board()
        self.dice = Dice()
        self.rounds = 0
        self.max_rounds = 10

    def start(self):
        """Start the game."""
        print("Welcome to the Game of Life!")
        self.setup_players()
        self.play()

    def setup_players(self):
        """Set up players."""
        while True:
            try:
                num_players = int(input("Enter number of players: "))
                if num_players < 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of players.")
        for i in range(num_players):
            while True:
                name = input(f"Enter name for player {i + 1}: ").strip()
                if name:
                    break
                print("Name cannot be empty.")
            self.players.append(Player(name))

    def play(self):
        """Main game loop."""
        while not self.is_over():
            self.rounds += 1
            print(f"\nRound {self.rounds}")
            for player in self.players:
                print(f"{player.name}'s turn.")
                input("Press Enter to roll dice...")
                steps = self.dice.roll()
                print(f"Rolled a {steps}!")
                self.board.move_player(player, steps)
                self.board.trigger_space(player)
                print(player.summary())
                cmd = input("Enter 'p' for summary, 'q' to quit, or press Enter to continue: ").lower()
                if cmd == 'p':
                    self.show_summary()
                elif cmd == 'q':
                    print("Game terminated early.")
                    return
        self.show_winner()

    def is_over(self) -> bool:
        """Determine if the game is over."""
        return self.rounds >= self.max_rounds

    def show_summary(self):
        """Display summary of all players."""
        for player in self.players:
            print(player.summary())

    def show_winner(self):
        """Determine and print winner."""
        winner = max(self.players, key=lambda p: p.money)
        print(f"Winner: {winner.name} with ${winner.money}")


if __name__ == "__main__":
    game = Game()
    game.start()