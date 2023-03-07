from collections import deque

# 4방향
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 세로, 가로
R, C = map(int, input().split())

# R줄, C개의 알파벳 정보
board = [input() for _ in range(R)]

# 방문 정보 저장
chk = [[set() for _ in range(C)] for _ in range(R)]

# 이동한 거리
ans = 0

# 방문 좌표
dq = deque()
# 첫번째 방문 처리 (알파벳 저장)
chk[0][0].add(board[0][0])
# 첫번째 방문 처리 (방문 좌표 저장)
dq.append((0, 0, board[0][0]))

def is_valid_coord(y, x) :
    return 0 <= y < R and 0 <= x < C


# 넓이 우선 탐색(4방향 탐색, BFS)
while len(dq) > 0 :
    y, x, s = dq.popleft()
    ans = max(ans, len(s))


    for k in range(4) :
        ny = y + dy[k]
        nx = x + dx[k]

        if is_valid_coord(ny, nx) and board[ny][nx] not in s :
            ns = s + board[ny][nx]
            
            if ns not in chk[ny][nx] :
                chk[ny][nx].add(ns)
                dq.append((ny, nx, ns))

print(ans)