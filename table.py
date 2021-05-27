from deck import makeDeck
import random
class Table:
    def __init__(self):
        self.list_of_players = []
        self.on_table= []
        self.deck = makeDeck()
       
        for i in range(0,4):
            self.on_table.append(self.deck.pop())
        
    #Repartir cartas#
    def deal(self):
        i = 0
        while i < 4:
            for player in self.list_of_players:
                player.hand.append(self.deck.pop())
            i += 1
    def score(self,plist):
    #Contando el score#
            loff_hand = []
            boff_hand = 0
            for player in plist:
                l=0
                loff_hand.append(len(player.off_hand))
                club_cards = 0
                number_of_cards = len(player.off_hand)
                if loff_hand[l] > boff_hand:
                    boff_hand = loff_hand[l]
                    l =+1
                    if loff_hand.count(boff_hand) == 1:
                        off_hand_points = loff_hand.index(boff_hand)
                        player.score += 2
                for i in player.off_hand:
                    if i.symbol == "Spades":
                        club_cards =+ 1
                    if i.value == 1 or i.name == "10_Diamonds" or i.name == "2_Spades":
                        player.score =+ 1
                player.off_hand = []
            self.on_table = []
            self.deck = makeDeck()
            for player in plist:
                print(player.score,player.name)
                