from collections import deque

dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

N = int(input())
chk = [[False] * N for _ in range(N)]

# 그래프 정보 입력받기 (adj, ans)

def is_valid_coord(y, x) :
    return 0 <= y < N and 0 <= x < N

def dfs(y, x) :
    if adj[y][x] == ans :
        return
    
    for k in range(4) :
        ny = y + dy[k]
        nx = x + dx[k]

        if is_valid_coord(ny, nx) and not chk[ny][nx] :
            chk[ny][nx] = True
            # 재귀호출
            dfs(ny, nx)

def bfs(sy, sx) :
    q = deque()
    chk[sy][sx] = True
    q.append((sy, sx))

    while len(q) :
        y, x = q.popleft()
        
        if adj[y][x] == ans :
            # 답을 찾으면 return
            return
        
        for k in range(4) :
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny, nx) and not chk[ny][nx] :
                chk[ny][nx] = True
                q.append(ny, nx)