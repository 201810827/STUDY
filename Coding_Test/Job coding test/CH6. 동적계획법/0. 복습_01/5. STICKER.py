# 스티커 1장 떼면 -> 스티커와 변을 공유하는 위, 아래, 좌, 우 스티커는 사용할 수 없음
# 스티커에 점수를 매겨 최대합이 되도록 스티커를 떼어낸다

# 테스트 케이스의 개수 T
T = int(input())

for _ in range(T) :
    # N (스티커의 개수)
    N = int(input())
    # N개의 정수 (스티커의 점수)
    sticker = [list(map(int, input().split())) for _ in range(2)]
    DP = [[0] * N for _ in range(2)]

    for i in range(2) :
        DP[i][0] = sticker[i][0]
        if i > 1 :
            DP[i][1] = sticker[i ^ 1][1] + sticker[i][1]

    for j in range(2, N) :
        for i in range(2) :
            DP[i][j] = max(DP[i ^ 1][j - 2], DP[i ^ 1][j - 1]) + DP[i][j]

    # 두 변을 공유하지 않는 스티커 점수의 최대값을 출력
    print(max(DP[0][N - 1], DP[1][N - 1]))