import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())

board = [[False] * (N + 1) for _ in range(N + 1)]
chk = [False] * (N + 1)

for _ in range(M) :
    u, v = map(int, input().split())
    board[u][v] = True
    board[v][u] = True

def dfs(y) :

    for x in range(1, N + 1) :
        if board[y][x] and not chk[x] :
            chk[x] = True
            dfs(x)

ans = 0
for i in range(1, N + 1) :
    if not chk[i] :
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)