class Build:
    def __init__(self,hand,on_table):
        self.value = 0
        self.cards = []
        self.cards.append(hand)
        self.value = self.value + hand.value
        self.cards.append(on_table)
        for x in on_table:
            self.value = self.value + x.value
            self.cards.append(x)

    def __repr__(self):
        return f"{self.value}"



