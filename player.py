class Player:
    def __init__(self,name):
        self.name = name
        self.score =0
        self.hand = []
        self.off_hand = []
    def play(self,table):
        card_playing = input("what card are you gonna play?")

        def check_cards(Input,list_of_cards):
            try:
                H = int(Input)
                if H < len(list_of_cards):
                    print("Success")
                    return list_of_cards[H]
                else:
                    print("Input is out of range")
                    self.play(table)
            except:
                for card in list_of_cards:
                    if Input == card.name:
                        print("Success")
                        return card
                print ("Card is not found")
                self.play(table)
        card_playing = check_cards(card_playing,self.hand)
