# 공간의 크기
n = int(input())
x, y = 1, 1
moves = input().split()

# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move in moves :
    for i in range(len(move_types)) :
        if move == move_types[i] :
            # 'L'이면 (1,1) + (0,-1)
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 넘어서면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동
    x, y = nx, ny

print(x, y)