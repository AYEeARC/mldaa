# 8 Queens Problem using Backtracking

N = 8

board = [[0 for _ in range(N)] for _ in range(N)]


def is_safe(row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):

    # All queens placed
    if row == N:
        return True

    for col in range(N):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Place first queen at row 0, column 0
board[0][0] = 1

if solve(1):

    print("8-Queens Solution:\n")

    for row in board:
        print(row)

else:
    print("No solution found.")