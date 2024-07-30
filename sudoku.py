def ispossible(board,row,col,val):
    for i in range(9):
        if(board[row][i]==str(val)):
            return False
        if(board[i][col]==str(val)):
            return False
        if(board[3*(row//3)+i//3][3*(col//3)+col%3]==str(val)):
            return False
    return True


def solve(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j]=='.'):
                for k in range(1,10):
                    if(ispossible(board,i,j,k)):
                        board[i][j]=str(k)
                        if(solve(board)==True):
                          return(True)
                        else:
                          board[i][j]='.'
                return False
    return True






board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solve(board)
print(board)