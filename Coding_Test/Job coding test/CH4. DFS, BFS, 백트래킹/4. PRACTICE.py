from collections import deque

# 4방향 이동
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 세로, 가로
R, C = map(int, input().split())
# 보드 정보
board = [input() for _ in range(R)]

# 방문 알파벳 저장
chk = [[set() for _ in range(C)] for _ in range(R)]
# 방문 좌표 저장
dq = deque()
# 이동 거리
ans = 0

# 첫번째 방문 처리
# 알파벳 저장
chk[0][0].add(board[0][0])
# 좌표 저장
dq.append((0, 0, board[0][0]))

def is_valid_coord(y, x) :
    return 0 <= y < R and 0 <= x < C


while dq :
    # 현재 위치 출력
    x, y, s = dq.popleft()
    # 4방향 중 가장 큰 값
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