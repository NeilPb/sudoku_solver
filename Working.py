board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard (board):

    for col in range (len(board)) :
        if col % 3 == 0 and col != 0:
            print("- - - - - - - - - - - ")
        for row in range (len(board[col])):
            if row % 3 == 0 and row != 0:
                print("| ",end="")
            if row == 8:
                print(board[col][row])
            else:
                print (str(board[col][row])+ " ",end="")

printBoard (board)