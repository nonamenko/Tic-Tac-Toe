def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    print("Ласкаво просимо до гри 'Крестики-нулики'!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for turn in range(9):
        print_board(board)
        print(f"Хід гравця {current_player}.")

        try:
            row, col = map(int, input("Введіть рядок і стовпчик (0-2) через пробіл: ").split())
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Гравець {current_player} переміг!")
                    return
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Клітинка вже зайнята. Спробуйте ще раз.")
        except (ValueError, IndexError):
            print("Некоректний ввід. Введіть два числа від 0 до 2.")

    print_board(board)
    print("Нічия!")

if __name__ == "__main__":
    tic_tac_toe()
