# M*N크기의 보드
# 몇 칸은 검은색 + 몇 칸은 흰색
# 이 보드를 8 * 8 크기로 만들고 싶음
# 서로 번갈아가면서 칠해져있어야함 ! (변을 공유하면 서로 다른 색이여야함)
# 두 가지 경우의 수 -> 1. 첫번째 칸이 검정색 2. 첫번째 칸이 하얀색

# 8*8로 잘라서 서로 색이 교차되게 하기 위해 다시 칠해야하는 정사각형의 최소 개수를 구하라


# M * N (8 <= M & N <= 50)
M, N = map(int, input().split())
# 각 보드의 행 (B = 검정, W = 흰색)
board = [input() for _ in range(N)]

ans = N * M   

def repaint(y, x, bw) :
    global ans
    cnt = 0

    for i in range(8) :
        for j in range(8) :

            if (i + j) % 2 :
                if board[y + i][x + j] == bw :
                    cnt += 1
            else :
                if board[y + i][x + j] != bw:
                    cnt += 1

    ans = min(ans, cnt)

         

for y in range(0, N - 7) :
    for x in range(0, M - 7) :
        repaint(y, x, 'B')
        repaint(y, x, 'W')

print(ans)