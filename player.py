from table import Table
from card import Card
from build import Build
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
                    return list_of_cards[H]
                else:
                    print("Input is out of range")
                    self.play(table)
            except:
                for card in list_of_cards:
                    if Input == card.name:
                        return card
                print ("Card is not found")
                self.play(table)
    
        def trail(card):
            table.on_table.append(card)
            self.hand.remove(card)
    
        def capture(card):
            card_to_capture = check_cards(input("What card do you want to capture?"),table.on_table)
            if card.value == card_to_capture.value:
                 self.off_hand.append(card)
                 self.off_hand.append(card_to_capture)
                 table.on_table.remove(card_to_capture)
                 self.hand.remove(card)
            else:
                print("The values are not the same")
                self.play(table)
        def build(card):
            number_of_cards = int(input("how many cards do you want to use? :"))
            building = []
            while number_of_cards > 0:
                card_to_build = check_cards(input("with wich card do you want to build?"),table.on_table)
                building.append(card_to_build)
                self.hand.remove(card)
                table.on_table.remove(card_to_build)
                number_of_cards =-1

            o = Build (card_playing,building)
            table.on_table.append(o)
        def options(option):
            if option == "trail":
                trail(card_playing)
            elif option =="capture" :
                capture(card_playing)
            elif option == "build":
                build(card_playing)
            else:
                self.play(table)
        
        card_playing = input("what card are you gonna play?")
        card_playing = check_cards(card_playing,self.hand)
        option = input("What you want to do with the card?(trail),(capture)")
        options(option)