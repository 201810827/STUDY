from collections import deque

# 가로, 세로
N, M = map(int, input().split())

# 미로
maze = [input() for _ in range(N)]
# 방문 체크
chk = [[False] * M for _ in range(N)]
dq = deque()

# 4방향
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 유효성 체크
def is_valid_coord(y, x) :
    return 0 <= y < N and 0 <= x < M


# 첫번째 방문 체크
dq.append((0, 0, 1))
chk[0][0] = True


# 넓이 우선 탐색(BFS)
while len(dq) :

    y, x, d = dq.popleft()

    # 미로 끝에 다달았는지 체크
    if y == N - 1 and x == M - 1 :
        print(d)
        break

    for k in range(4) :
        ny = y + dy[k]
        nx = x + dx[k]
        nd = d + 1

        if is_valid_coord(ny, nx) and not chk[ny][nx] and maze[ny][nx] == '1' :
            chk[ny][nx] = True
            dq.append((ny, nx, nd))