# N*N 체스판, N개의 퀸
N = int(input())

# 체스판
board = [[False] * N for _ in range(N)]

# 경우의 수
cnt = 0


# 열 검사
def rowchecking(y, x) :
    for i in range(1, y + 1) :
        if board[y - i][x] :
            return True
        
    return False

# 대각선 검사
def digonalchecking(y, x) :
    for i in range(1, y + 1) :
        if 0 <= x - i and board[y - i][x - i] :
            return True
        if x + i < N and board[y - i][x + i] :
            return True
        
    return False

# 백트래킹
def backtracking(i) :
    global cnt

    if i >= N :
        cnt += 1
        return
    
    for j in range(N) :
        if not rowchecking(i, j) and not digonalchecking(i, j) :
            board[i][j] = True
            backtracking(i + 1)
            board[i][j] = False

backtracking(0)
print(cnt)