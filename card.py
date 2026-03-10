import random

class Card:
    careers = [
        ("Engineer", 5000),
        ("Doctor", 7000),
        ("Teacher", 4000),
        ("Lawyer", 6000)
    ]

    actions = [-2000, -1000, 1000, 2000, 3000]

    @staticmethod
    def draw_career():
        return random.choice(Card.careers)

    @staticmethod
    def draw_action():
        return random.choice(Card.actions)