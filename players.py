class Players:
    def __init__(self,name):
        self.name = name
        self.score =0
        self.hand = []
        self.off_hand = []
    def play(self,table):
      card_playing = input("what card are you gonna play?")
      def check_cards(Input,list_of_cards):
        for card in list_of_cards:
            if Input == card.name:
                return card
        print ("Card is not found")
