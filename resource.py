from round_counter import Round

class Resuorse:
    '''
    a class representation of resourses
    '''
    def __init__(self, quantity):
        self.resourse_name = ""
        self.penalty_name = ""
        self.quantity = quantity
        self.card_limit = 0
        self.base_chance = 0
        self.chance_per_card = 0
        self.chance_per_turn = 0
        self.overdraw_turn = 0
        self.penalty_card = ""

    def penalty_chance(self):
        '''
        penalty activates if you have too many cards of certain type
        return: chance to take penalty card

        '''
        # round = Round
        penalty_chance = 0
        if self.quantity > self.card_limit:
            penalty_chance = self.base_chance + (self.quantity - self.card_limit)*self.chance_per_card + (Round().get - self.overdraw_turn)*self.chance_per_turn
        return penalty_chance

    def add(self, number):
        '''
        adds a number of cards of certain type
        '''
        self.quantity += number

    def remove(self, number):
        '''
        removes a number of cards of certain type
        '''
        self.quantity -= number

    def set(self, number):
        self.quantity = number

    def get(self):
        return self.quantity

    def __str__(self):
        return "You have {0} cards, type: {1}".format(self.quantity, self.resourse_name)

class Artefact(Resuorse):
    '''
    a class representation of artifacts(parent class - Resourse)
    '''
    def __init__(self, quantity):
        self.resourse_name = "Artifacts"
        self.penalty_card = "Lazines"
        self.card_limit = 3
        self.base_chance = 10
        self.chance_per_card = 10
        self.chance_per_turn = 5
        super().__init__(quantity)

class Minion(Resuorse):
    '''
    a class representation of minions(parent class - Resourse)
    '''
    def __init__(self, quantity):
        self.resourse_name = "Minions"
        self.penalty_card = "Pride"
        self.card_limit = 10
        self.base_chance = 10
        self.chance_per_card = 2
        self.chance_per_turn = 1
        super().__init__(quantity)

class Food(Resuorse):
    '''
    a class representation of food(parent class - Resourse)
    '''
    def __init__(self, quantity):
        self.resourse_name = "Food"
        self.penalty_card = "Gluthony"
        self.card_limit = 8
        self.base_chance = 10
        self.chance_per_card = 2
        self.chance_per_turn = 6
        super().__init__(quantity)

class Money(Resuorse):
    '''
    a class representation of money(parent class - Resourse)
    '''
    def __init__(self, quantity):
        self.resourse_name = "Money"
        self.penalty_card = "Greed"
        self.card_limit = 10
        self.base_chance = 10
        self.chance_per_card = 6
        self.chance_per_turn = 2
        super().__init__(quantity)

class Suspicion(Resuorse):
    '''
    a class representation of suspicion(parent class - Resourse)
    '''
    def __init__(self, quantity):
        self.resourse_name = "Suspicion"
        self.penalty_card = "Wrath"
        self.card_limit = 0
        self.card_limit_big = 4
        self.base_chance = 0
        self.chance_per_card = 3
        self.chance_per_card_big = 5
        self.chance_per_turn = 1
        super().__init__(quantity)

    def penalty_chance(self):
        penalty_chance=0
        if self.quantity > self.card_limit:
            penalty_chance = self.base_chance + max((self.quantity - self.card_limit),self.card_limit_big)*self.chance_per_card + (Round().get - self.overdraw_turn)*self.chance_per_turn
        if self.quantity > self.card_limit_big:
            penalty_chance += (self.quantity - self.card_limit_big)*self.chance_per_card_big
        return penalty_chance


