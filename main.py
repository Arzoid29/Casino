from player import Player
from table import Table

if __name__ == '__main__':
    player1 = Player("Player1")
    table = Table()
    table.list_of_players = Player.plist
    
    
    while True:
        while True:
            if table.deck == []:
                table.score(Player.plist)
            a = 3
            table.deal()
            while a >= 0:
                for p in Player.plist:
                    print(table.on_table)
                    print(player1.hand)
    
                    p.play(table)
    
                    print(table.on_table)
                    print(player1.hand)
                    print(player1.off_hand)
                a -= 1
    