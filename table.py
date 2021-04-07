from deck import makeDeck
class Table:
    def __init__(self):
        self.list_of_players = []
        self.on_table= []
        self.deck = makeDeck()
    def deal(self):
        i = 0
        while i < 4:
            for player in self.list_of_players:
                player.hand.append(self.deck.pop())
            i += 1