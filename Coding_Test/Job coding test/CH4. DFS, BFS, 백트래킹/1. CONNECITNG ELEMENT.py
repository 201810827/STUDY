import sys

input = sys.stdin.readline

# 정점 개수 N, 간선의 개수 M
N, M = map(int, input().split())

# 간선의 정점 u, v
element = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M) :
    u, v = map(int, input().split())
    element[u][v] = True
    element[v][u] = True

ans = 0
chk = [False] * (N + 1)

# DFS(깊이 우선 검색)
def dfs(i) :
    for j in range(1, N + 1) :
        if element[i][j] and not chk[j] :
            chk[j] = True
            dfs(j)

# 방문 체크
for i in range(1, N + 1) :
    if not chk[i] :
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)            