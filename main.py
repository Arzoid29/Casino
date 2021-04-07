from player import Player
from table import Table

if __name__ == '__main__':
    player1 = Player("Player1")
    table = Table()
    table.list_of_players = Player.plist
    
    table.deal()
    
    print(table.on_table)
    print(player1.hand)
    
    player1.play(table)
    
    print(table.on_table)
    print(player1.hand)
    print(player1.off_hand)
    