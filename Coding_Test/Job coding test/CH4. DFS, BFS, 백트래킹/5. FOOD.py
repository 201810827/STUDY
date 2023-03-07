import sys
sys.setrecursionlimit(10 ** 6)

# 4방향
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 세로, 가로, 음식물 개수
N, M, K = map(int, input().split())

# 음식물 좌표 정보
adj = [['.'] * (M) for _ in range(N)]
for _ in range(K) :
    r, c = map(int, input().split())
    adj[r - 1][c - 1] = '#'

# 방문 체크 배열
chk = [[False] * M for _ in range(N)]
# 크기
ans = 0
test = 0

def is_valid_coord(y, x) :
    return 0 <= y < N and 0 <= x < M

# 깊이우선탐색(DFS) + 넓이우선탐색(BFS)
def dfs(y, x) :
    global test, ans
    chk[y][x] = True
    test += 1
    ans = max(ans, test)
    
    for k in range(4) :
        ny = y + dy[k]
        nx = y + dx[k]

        if is_valid_coord(ny, nx) and not chk[ny][nx] and adj[ny][nx] == '#' :
            dfs(ny, nx)

for i in range(N) :
    for j in range(M) :
        if not chk[i][j] and adj[i][j] == '#' :
            test = 0
            dfs(i, j)

print(ans)