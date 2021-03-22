class Card :
    value_to_letters = {
        1: "A",
        11: "J",
        12: "Q",
        13: "K"
    }
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol
        try:
            self.name = Card.value_to_letters[value] + "_" + symbol
        except:
            self.name = str(value) + "_" + symbol
    def __repr__(self):
        return f"{self.name}"




