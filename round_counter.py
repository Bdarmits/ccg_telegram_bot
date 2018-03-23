class Round:
    def __init__(self):
        self.round_num = 0

    def next_round(self):
        self.round_num += 1
        return self.round_num
    @property
    def get(self):
        return self.round_num
