from player import Player
from board import Board
from dice import Dice

class Game:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.dice = Dice()
        self.game_over = False

    def start(self):
        self.setup_players()
        self.game_loop()

    def setup_players(self):
        while True:
            try:
                num = int(input("Enter number of players (2-4): "))
                if 2 <= num <= 4:
                    break
                else:
                    print("Please enter between 2 and 4 players.")
            except ValueError:
                print("Invalid input.")

        for i in range(num):
            while True:
                name = input(f"Enter name for player {i+1}: ").strip()
                if name:
                    self.players.append(Player(name))
                    break
                else:
                    print("Name cannot be empty.")

    def game_loop(self):
        while not self.game_over:
            for player in self.players:
                if player.retired:
                    continue

                print(f"\n{player.name}'s turn.")
                command = input("Press Enter to roll dice or 'p' for summary: ")

                if command.lower() == 'p':
                    self.print_summary()
                    continue

                roll = self.dice.roll()
                print(f"{player.name} rolled {roll}")

                player.move(roll, self.board.size)
                print(self.board.check_space(player))

                if player.retired:
                    print(f"{player.name} has retired!")

            if all(p.retired for p in self.players):
                self.end_game()

    def print_summary(self):
        print("\n--- Game Summary ---")
        for player in self.players:
            print(player.summary())

    def end_game(self):
        self.game_over = True
        winner = max(self.players, key=lambda p: p.money)
        print("\nGame Over!")
        print(f"The winner is {winner.name} with £{winner.money}")