location = input()
# 행 위치 입력
row = int(location[1])
# 열 위치 입력
# ord() = 아스키 코드 변환 함수

column = int(ord(location[0])) - int(ord('a')) + 1

# 8가지 방향
steps = [(-2, -1), (-1, -2), (1. -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
# 이동 방향 검사
for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1

print(result)