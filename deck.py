#Making the deck with a ramdom position#
from card import Card
import random as rd
def makeDeck():
    deck = []
    symbols = ["Hearts","Diamonds","Spades","Clubs"]
    for symbol in symbols:
        for value in range(1,14):
         deck.append(Card(value,symbol))
    return rd.sample(deck,k = 52)
    