def safe(col, row, n, board):
    # Check this row on the left side
    c = col
    while c >= 0:
        if board[row][c] == 'Q':
            return False
        c -= 1

    # Check upper diagonal on the left side
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1

    # Check lower diagonal on the left side
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 'Q':
            return False
        r += 1
        c -= 1

    return True

def queen(col, n, board, ans):
    if col == n:
        ans.append([row[:] for row in board])
        return
    
    for row in range(n):
        if safe(col, row, n, board):
            board[row][col] = 'Q'
            queen(col + 1, n, board, ans)
            board[row][col] = '.'

n = 4
board = [["." for _ in range(n)] for _ in range(n)]
ans = []
queen(0, n, board, ans)

for solution in ans:
    for row in solution:
        print(" ".join(row))
    print()
#higher time complexity since 3 while loop