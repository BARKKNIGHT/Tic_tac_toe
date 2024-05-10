# Display some instructions to play the game

def intro():
    print("Welcome to the game of tic tac toe")
    print("Following are the numbers corresponding place on the board")
    example = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(example[7] + " | " + example[8] + " | " + example[9])
    print("--|---|--")
    print(example[4] + " | " + example[5] + " | " + example[6])
    print("--|---|--")
    print(example[1] + " | " + example[2] + " | " + example[3])
    print("You may enter the number to place 'X' or 'O' in your turn")
def name_share(player_1,player_2):
    global player_name_1
    player_name_1=player_1
    global player_name_2
    player_name_2=player_2
Player_Options = ['X', 'O']   # A list for cross-checking inputs

moves = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ",]  # To record all the moves of the players

played = []  # Positions that have already been played

allowed_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# select 'X' or 'O'

def select_player1(moves, played, allowed_moves):
    player1 = "q"

    while player1 not in Player_Options:
        player1 = input(f"{player_name_1} ('X' or 'O'):")
        player1=player1.upper()
        if player1 not in Player_Options:
            print("Oops! Seems like you entered an invalid option")

    select_player2(player1, moves,played, allowed_moves)


def select_player2(player1, moves, played, allowed_moves):

    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'

    print(f"{player_name_1} is {player1}")
    print(f"{player_name_2} is {player2}")

    display(moves)
    play(played, allowed_moves, player1, player2,1, moves)

# For displaying the board after every turn :]

def display(moves):
    print(moves[7] + " | " + moves[8] + " | " + moves[9])
    print("--|---|--")
    print(moves[4] + " | " + moves[5] + " | " + moves[6])
    print("--|---|--")
    print(moves[1] + " | " + moves[2] + " | " + moves[3])

# Take input from player 1

def play(played, allowed_moves, player1, player2, player, moves):
    if(player==1):

        move_played = "q"

        next_play = 2

        while move_played.isdigit() == False or move_played not in allowed_moves or move_played in played:
            move_played = input(f"{player_name_1}'s Turn (1-9):")

            if move_played.isdigit() == False or move_played not in allowed_moves or move_played in played:
                print("Oops! Seems like you entered an invalid move \nEnter a valid digit!")

        int_move_played = int(move_played)
        moves[int_move_played] = player1
        played.append(move_played)

        display(moves)

        win_condition(moves, player1, player2, played, allowed_moves, next_play)
    elif(player==2):
            move_played = "q"

            next_play = 1


            while move_played.isdigit() == False or move_played not in allowed_moves or move_played in played:
                move_played = input(f"{player_name_2}'s Turn (1-9):")

            if move_played.isdigit() == False or move_played not in allowed_moves or move_played in played:
                print("Oops! Seems like you entered an invalid move \nEnter a valid digit!")

            int_move_played =  int(move_played)
            moves[int_move_played] = player2
            played.append(move_played)

            display(moves)
            win_condition(moves, player1, player2, played, allowed_moves, next_play)




def win_condition(moves, player1, player2, played, allowed_moves, next_play):
    n = 1
    while n < 8:
        if moves[n] == moves[n+1] == moves[n+2] == player1:  # For checking horizontal
            print(f"{player_name_1} won (horizontal)")
            print(f"Sometimes you are never meant to win {player_name_2}!!")
            return None

        elif moves[n] == moves[n+1] == moves[n+2] == player2:  # For checking horizontal
            print(f"{player_name_2} won (horizontal)")
            print("👀👀")
            return None

        n = n + 3

    n = 1
    while n < 4:

        if moves[n] == moves[n+3] == moves[n+6] == player1:  # For checking vertical
            print(f"{player_name_1} won (vertical)")
            print(f"Sometimes you are never meant to win {player_name_2}!!")
            return None

        elif moves[n] == moves[n+3] == moves[n+6] == player2:  # For checking vertical
            print(f"{player_name_2} won (vertical)")
            return None

        n = n + 1

    n = 1

    if moves[n] == moves[n+4] == moves[n+8] == player1:  # For checking diagonal \
        print(f"{player_name_1}won (diagonal)")
        print("👀👀")


    elif moves[n] == moves[n+4] == moves[n+8] == player2:  # For checking diagonal \
        print(f"{player_name_2} won (diagonal)")

    elif moves[n+2] == moves[n+4] == moves[n+6] == player1:  # For checking diagonal /
        print(f"{player_name_2} won (diagonal)")
        print(f"Sometimes you are never meant to win {player_name_1}!!")

    elif moves[n+2] == moves[n+4] == moves[n+6] == player2:  # For checking diagonal /
        print(f"{player_name_2} won (diagonal)")

    elif len(played) == len(allowed_moves):
        print("It's a tie!!")
        print("👀👀")


    elif next_play == 1:
        play(played, allowed_moves, player1, player2, 1, moves)

    elif next_play == 2:
        play(played, allowed_moves, player1, player2, 2, moves)


# Wanna play again? 👀👀

def play_again():
    again = "M"
    while again not in ["Y", "N"]:
        again = input("Play again? (Y or N):")
        again=again.upper()
        if again not in ["Y", "N"]:
            print("Oops! Seems like you entered an invalid option")

    if again == 'N':
        return "Thanks for playing :)"
    else:
        return 'Y'


