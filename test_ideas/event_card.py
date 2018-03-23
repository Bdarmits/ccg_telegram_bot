from card1_options import *

class Event_card:
    def __init__(self, opt1, opt2, opt3):
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        self.card_name = ""
        self.card_description = ""

class Card1(Event_card):
    def __init__(self, opt1 = Opt1, opt2 = Opt2, opt3 = Opt3):
        self.card_name = "Farm"
        self.card_description = "Send your people to work, we need food"
        super().__init__(opt1, opt2, opt3)

    def option_action(self):
        choose = int(input("Choose one of the three options(1/2/3): "))
        if choose == 1:
            self.opt1.effect()
        if choose == 2:
            self.opt2.effect()
        if choose == 3:
            self.opt3.effect()


# test
event = Card1
event().option_action()
print(minion.quantity)
print(food.quantity)


