from collections import deque

# N * M 크기 배열
N, M = map(int, input().split())

# 미로
maze = [input() for _ in range(N)]
# 방문 체크
chk = [[False] * M for _ in range(N)]

# 4방향
dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

def is_valid_coord(y, x) :
    return 0 <= y < M and 0 <= x < N



q = deque()
q.append((0, 0, 0))
chk[0][0] = True

while len(q) > 0 :

    y, x, d = q.popleft()

    if y == N - 1 and x == M - 1 :
        print(d)
        break
        
    for k in range(4) :
        ny = y + dy[k]
        nx = x + dx[k]
        nd = d + 1

        if is_valid_coord(ny, nx) and maze[ny][nx] == '1' and not chk[ny][nx] :
            chk[ny][nx] = True
            q.append((ny, nx, nd))