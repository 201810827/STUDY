# 행, 열 위치
n, m = map(int, input().split())

# 현재 위치 설정
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
# 방문 처리
d[x][y] = 1

# 방향 처리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 맵 정보
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

# 왼쪽 회전
def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

count = 1
turn_time = 0
while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 칸 여부
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else :
        turn_time += 1
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        else :
            break
        turn_time = 0

print(count)
    