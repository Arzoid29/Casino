from player import Player
from table import Table

if __name__ == '__main__':
    player1 = Player("Player1")
    table = Table()
    table.list_of_players = Player.plist
    
    Status = True
    while Status:
        if table.deck == []:
            table.score(Player.plist)
            table.dealTable()
        a = 3
        table.deal()
        while a >= 0:
            for p in Player.plist:
                print("Table")
                print(table.on_table)
                print("\n")
                print("Player Hand")
                print(player1.hand)
                print("\n")
    
                p.play(table)

                print("Table")
                print(table.on_table)
                print("\n")
                print("Player Hand")
                print(player1.hand)
                print("\n")
                print("Player off hand")
                print(player1.off_hand)
                print("\n")
            a -= 1
        for player in Player.plist:
            if player.score >= 21:
                print(f"The game is over winner is {player.name}")
                Status = False
    print("Results")
    for player in Player.plist:
        print(player.name , player.score)