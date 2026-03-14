class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 10000
        self.retired = False

    def move(self, steps, board_size=25):
        self.position = (self.position + steps) % board_size

    def add_money(self, amount):
        self.money += amount

    def lose_money(self, amount):
        self.money -= amount

    def assign_career(self, career, salary):
            self.career = career
            self.salary = salary

    def get_status(self):
        return f"{self.name} | Position: {self.position} | Money: ${self.money}"