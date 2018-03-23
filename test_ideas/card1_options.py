'''
3 options:
    1st: - 1minions, + 2food
    2nd: -2 minions, + 4food
    3rd: - None, + None
'''

from resource import Minion, Food

'''
in fututre i will import from playe's, resourses
now , test version
'''
minion = Minion(3)
food = Food(0)

class Opt1:
    def __init__(self):
        self.description = "you sent 1 minion to work"

    @staticmethod
    def effect():
        minion.remove(1)
        food.add(2)


class Opt2:
    def __init__(self):
        self.description = "you sent 2 minions to work"

    @staticmethod
    def effect():
        minion.remove(2)
        food.add(4)


class Opt3:
    def __init__(self):
        self.description = "nu ti i pidor"

    @staticmethod
    def effect():
        pass