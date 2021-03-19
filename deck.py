from card import Card
def makeDeck():
    deck = []
    symbols = ["Hearts","Diamonds","Spades","Clubs"]
    for symbol in symbols:
        for value in range(1,14):
         deck.append(Card(value,symbol))
    return deck
D = makeDeck()
