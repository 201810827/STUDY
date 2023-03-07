from collections import deque
import sys

input = sys.stdin.readline

# 4방향
dy = (2, 1, -2, -1, 2, 1, -2, -1)
dx = (1, 2, 1, 2, -1, -2, -1, -2)
N = 0

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

# 테스트 케이스 개수
K = int(input())

# 한 변의 길이, 출발점, 도착점
for _ in range(K) :
    N = int(input())
    dq = deque()
    visited = [[False] * N for _ in range(N)]
    # 출발
    y, x = map(int, input().split())
    # 도착
    c, r = map(int, input().split())

    # 출발지 체크
    visited[y][x] = True
    dq.append((y, x, 0))

    while dq :
        y1, x1, d = dq.popleft()
        if y1  == c and x1 == r :
            print(d)
            break

        for k in range(8) :
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1

            if is_valid_coord(ny, nx) and not visited[ny][nx] :
                visited[ny][nx] = True
                dq.append((ny, nx, nd))
