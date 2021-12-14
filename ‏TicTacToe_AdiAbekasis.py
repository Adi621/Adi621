# Function to print Tic Tac Toe
import random
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t           SCOREBOARD           ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")


# Function to check if any player has won
def check_win(player_pos, cur_player):
    # All possible winning combinations
            # Bottom    # Mid       # Top     # Left    # Mid(ver)  # Right    # Diag     # Diag
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False

# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False

def choice_func(cur_player):
    while True:

        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for quit")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
            return choice

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
            return choice

        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            return choice

        else:
            print("Wrong Choice!!!! Try Again\n")

# Smart move function for each turn
def smartmove(possiblemoves, values, m):
    if m == 'O':
        y = 'X'
    y = 'O'
    com_pos = {m:[]}
    player_pos = {y:[]}

    # Check where the O AND X
    for i in range(0,9):
        if values[i] == m:
            com_pos[m].append(i+1)
        elif values[i] != m and values[i] != ' ': player_pos[y].append(i+1)

    # Start with the corners
    if len(possiblemoves) > 7:
        for i in [0, 2, 6, 8]:
            if i in possiblemoves: return i + 1

    # Check for winning
    for i in possiblemoves:
        com_pos[m].append(i + 1)
        if check_win(com_pos, m):
            return i + 1
        else: continue

    # Check for loosing
    for i in possiblemoves:
        player_pos[y].append(i+1)
        if check_win(player_pos, y):
            return i + 1
        else: continue

# Function for a single game of Tic Tac Toe
def single_game(cur_player):
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)

        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != ' ':
            print("Place already filled. Try again!!")
            continue

        # Update game information
        # Updating grid status
        values[move - 1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

# Function of every single game vs the PC
def single_gameComputer(cur_player):

    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Loop for single game
    while True:
        print_tic_tac_toe(values)

        # Try exception block for MOVE input
        try:
            print("Player ", player1, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != ' ':
            print("Place already filled. Try again!!")
            continue

        # Updating player positions
        player_pos[cur_player].append(move)

        # Update game information
        # Updating grid status
        values[move - 1] = cur_player

        # Function call for checking win about user
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print(f"Player {cur_player} has won the game!!")
            print("\n")
            return cur_player

        # Loop for check about clear places
        possiblemoves = []
        for i in range(0, 9):
            if values[i] == ' ':
                possiblemoves.append(i)
        randommove = 0
        if len(possiblemoves) == 0:

            # Check for draw if the board is full
            if check_draw(player_pos):
                print_tic_tac_toe(values)
                print("Game Drawn")
                print("\n")
                return 'D'

        # Check if is the first move and random move first
        # if len(player_pos[cur_player]) == 0:
        #     Simple move
        #     randommove = random.choice(possiblemoves)

        # Smart move
        # Updating computer positions

        if cur_player == 'O':
            randommove = smartmove(possiblemoves, values, 'X')
            player_pos['X'].append(randommove)
            values[randommove - 1] = 'X'

            # Function call for checking win about X
            if check_win(player_pos, 'X'):
                print_tic_tac_toe(values)
                print("Player X has won the game!!")
                print("\n")
                return 'X'

        else:
            randommove = smartmove(possiblemoves, values, 'O')
            player_pos['O'].append(randommove)
            values[randommove - 1] = 'O'

            # Function call for checking win about O
            if check_win(player_pos, 'O'):
                print_tic_tac_toe(values)
                print("Player O has won the game!!")
                print("\n")
                return 'O'

        # Another check for draw option
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
#--------------------------------START--------------------------------------
print("       HOW TO PALY?         ")
print("  PRESS THE NUMBERS BELOW  :")
print("   7   |    8    |    9    ")
print("       |         |         ")
print("-------------------------- ")
print("   4   |    5    |    6    ")
print("       |         |         ")
print("-------------------------- ")
print("   1   |    2    |    3    ")
print("       |         |         ")


# Asking the user about friend or PC game
choise = (input('Press 1 if you want to play vs friend or any other button to play vs the PC:'))

# The user will play vs friend
if choise == '1':
    if __name__ == "__main__":

        print("Player 1")
        player1 = input("Enter the name : ")
        print("\n")

        print("Player 2")
        player2 = input("Enter the name : ")
        print("\n")

        # Stores the player who chooses X and O
        cur_player = player1

        # Stores the choice of players
        player_choice = {'X': "", 'O': ""}

        # Stores the options
        options = ['X', 'O']

        # Stores the scoreboard
        score_board = {player1: 0, player2: 0}
        print_scoreboard(score_board)

        while True:
            # Call to choose X or O
            choice = choice_func(cur_player)

            # If the user choose to stop the game
            if choice == 3:
                print("Good bye!!")
                break

            # Stores the winner in a single game of Tic Tac Toe
            winner = single_game(options[choice - 1])

            # Edits the scoreboard according to the winner
            if winner != 'D':
                player_won = player_choice[winner]
                score_board[player_won] += 1
            print_scoreboard(score_board)

            # Switch player who chooses X or O
            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1

# The user will play vs the PC
else:
    if __name__ == "__main__":

        print("Player 1")
        player1 = input("Enter the name : ")
        print("\n")
        player2 = 'computer'

        # Stores the player who chooses X and O
        cur_player = player1

        # Stores the choice of players
        player_choice = {'X': "", 'O': ""}

        # Stores the options
        options = ['X', 'O']

        # Stores the scoreboard
        score_board = {player1: 0, player2: 0}
        print_scoreboard(score_board)

        while True:
            # Call to choose X or O
            choice = choice_func(cur_player)

            # If the user choose to stop the game
            if choice == 3:
                print("Good bye!!")
                break

            # Stores the winner in a single game of Tic Tac Toe
            winner = single_gameComputer(options[choice - 1])

            # Edits the scoreboard according to the winner
            if winner != 'D':
                player_won = player_choice[winner]
                score_board[player_won] += 1
            print_scoreboard(score_board)