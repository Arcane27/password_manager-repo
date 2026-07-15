board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                return row, column
    return None

print(find_empty(board))

def replace_spot(board, row, column, replacement):
    board[row][column] == replacement

# for i in range(9):
#     replace_spot(board, find_empty(board)[0], find_empty(board)[1], "X")
#     print(board)
replace_spot(board, find_empty(board)[0], find_empty(board)[1], "X")


print(board)



