class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 10000

    def move(self, steps):
        self.position += steps

    def add_money(self, amount):
        self.money += amount

    def lose_money(self, amount):
        self.money -= amount

    def get_status(self):
        return f"{self.name} | Position: {self.position} | Money: ${self.money}"