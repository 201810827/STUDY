N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = N * M

def make_acc(bw) :
    global ans
    # 누적합
    acc = [[0] * M for _ in range(N)]

    for i in range(N) :
        for j in range(M) :
            if i > 0 :
                acc[i][j] += acc[i - 1][j]
            if j > 0 :
                acc[i][j] += acc[i][j - 1]
            if i > 0 and j > 0 :
                acc[i][j] -= acc[i - 1][j - 1]
            if (i + j) % 2 and board[i][j] == bw :
                acc[i][j] += 1
            if (i + j) % 2 == 0 and board[i][j] != bw :
                acc[i][j] += 1

    for i in range(N - 7) :
        for j in range(M - 7) :
            cnt = acc[i + 7][j + 7]
            if i > 0 :
                cnt -= acc[i - 1][j + 7]
            if j > 0 :
                cnt -= acc[i + 7][j - 1]
            if i > 0 and j > 0 :
                cnt += acc[i - 1][j - 1]

            ans = min(ans, cnt)

make_acc('B')
make_acc('W')
print(ans)