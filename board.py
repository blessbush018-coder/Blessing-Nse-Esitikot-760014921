from card import Card

class Board:
    def __init__(self):
        self.size = 20
        self.special_spaces = {
            3: "career",
            7: "action",
            12: "action",
            18: "action"
        }

    def check_space(self, player):
        if player.position in self.special_spaces:
            space_type = self.special_spaces[player.position]

            if space_type == "career":
                career, salary = Card.draw_career()
                player.assign_career(career, salary)
                return f"{player.name} got career {career} with bonus £{salary}"

            elif space_type == "action":
                amount = Card.draw_action()
                player.add_money(amount)
                if amount >= 0:
                    return f"{player.name} gained £{amount}"
                else:
                    return f"{player.name} lost £{abs(amount)}"

        return "Nothing happened."