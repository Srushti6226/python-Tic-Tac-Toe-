from typing import Union

# Tic Tac Toe game in Python

BOARD_SIZE = 9

def print_board(board: list[str]) -> None:
    """
    Prints the Tic Tac Toe board.
    """
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def check_win(board: list[str]) -> Union[str, None]:
    """
    Checks if there is a winner or a tie.
    """
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return None

def game() -> None:
    """
    Plays the Tic Tac Toe game.
    """
    board = [' ' for _ in range(BOARD_SIZE)]
    current_player = 'X'
    while True:
        print_board(board)
        while True:
            try:
                move = int(input("Player {}, enter your move (1-{}): ".format(current_player, BOARD_SIZE)))
                if 1 <= move <= BOARD_SIZE and board[move - 1] == ' ':
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input, try again.")
        board[move - 1] = current_player
        result = check_win(board)
        if result:
            print_board(board)
            if result == 'Tie':
                print("It's a tie!")
            else:
                print("Player {} wins!".format(result))
            break
        current_player = 'O' if current_player == 'X' else 'X'

def main() -> None:
    """
    Main function.
    """
    game()

if __name__ == '__main__':
    main()