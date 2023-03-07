# BOTTOP-UP

# T개의 테스트케이스
T = int(input())
for _ in range(T) :
    # n개의 열
    N = int(input())
    STICKER = [list(map(int, input().split())) for _ in range(2)]
    DP = [[0] * N for _ in range(2)]

    for i in range(2) :
        DP[i][0] = STICKER[i][0]
        if i > 1 :
            DP[i][1] = STICKER[i ^ 1][1] + STICKER[i][1]

    for j in range(2, N) :
        for i in range(2) :
            DP[i][j] = max(DP[i ^ 1][j - 2], DP[i ^ 1][j - 1]) + DP[i][j]

    print(max(DP[0][N - 1], DP[1][N - 1]))