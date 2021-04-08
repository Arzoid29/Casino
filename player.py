from table import Table
class Player:
    plist = []
    def __init__(self,name):
        self.name = name
        self.score =0
        self.hand = []
        self.off_hand = []
        Player.plist.append(self)
    def play(self,table):

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
        def trail(card):
            table.on_table.append(card)
            self.hand.remove(card)
        
        
        card_playing = input("what card are you gonna play?")
        card_playing = check_cards(card_playing,self.hand)
        option = input("What you want to do with the card?(trail)")

        def options(option):
            if option == "trail":
                trail(card_playing)
            elif option =="":
                pass
        options(option)
        