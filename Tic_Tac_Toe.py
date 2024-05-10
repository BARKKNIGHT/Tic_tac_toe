import game 
def main():
    again = "Y"
    while again == "Y":
        Player_Options = ['X', 'O']  # A list for cross-checking inputs

        moves = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]  # To record all the moves of the players

        played = []  # Positions that have already been played

        allowed_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # To cross-check the move is valid

        game.intro()
        global player_name_1
        global player_name_2
        player_name_1=input("Enter name of player 1:")
        player_name_2=input("Enter name of player 2:")
        game.name_share(player_name_1,player_name_2)
        game.select_player1(moves, played, allowed_moves)
        again = game.play_again()

main()