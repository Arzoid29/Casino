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
            cards_amount = []
            biggest_amount = 0
            spades_amount = []
            biggest_spades_amount = 0
            for player in plist:
                spades_cards = 0
                for card in player.off_hand:
                    if card.symbol == "Spades":
                        spades_cards =+ 1
                        if card.value == 2:
                            player.score +=1
                    if card.value == 1:
                        player.score += 1
                    if card.name =="10_Diamonds":
                        player.score += 2
                player.off_hand = []
                
                spades_amount.append(spades_cards)
                cards_amount.append(len(player.off_hand))
                
                if cards_amount[-1] > biggest_amount:
                    biggest_amount = cards_amount[-1]
                
               
                if spades_amount[-1] > spades_cards:
                    spades_cards = spades_amount[-1]
                

            if cards_amount.count(biggest_amount) == 1:
                off_hand_points = cards_amount.index(biggest_amount)
                plist[off_hand_points].score += 2
                    
            if spades_amount.count(spades_cards) == 1:
                spades_points =spades_amount.index(spades_cards)
                plist[spades_points].score += 2


            
            self.on_table =[]
            self.deck = makeDeck()
            for player in plist:
                print(player.score,player.name)
