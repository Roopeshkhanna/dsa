def queen(col, n, board, leftrow, upperdiagonal, lowerdiagonal, ans):
    if col == n:
        ans.append([row[:] for row in board])
        return
    
    for row in range(n):
        if (not leftrow[row] and not upperdiagonal[n - 1 + col - row] and not lowerdiagonal[col + row]):
            leftrow[row] = True
            upperdiagonal[n - 1 + col - row] = True
            lowerdiagonal[col + row] = True

            board[row][col] = 'Q'
            queen(col + 1, n, board, leftrow, upperdiagonal, lowerdiagonal, ans)
            board[row][col] = '.'
            leftrow[row] = False
            upperdiagonal[n - 1 + col - row] = False
            lowerdiagonal[col + row] = False

n = 4
board = [["." for _ in range(n)] for _ in range(n)]
ans = []
lowerdiagonal = [False] * (2 * n - 1)
leftrow = [False] * n
upperdiagonal = [False] * (2 * n - 1)
queen(0, n, board, leftrow, upperdiagonal, lowerdiagonal, ans)

for solution in ans:
    for row in solution:
        print(" ".join(row))
    print()
#checking through array the time taken is O(1)