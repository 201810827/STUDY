N = int(input())

ans = 0

# i번째 열에 퀸을 두었는지 체크하는 배열
col = [False] * N
# \ 대각선을 체크하는 배열, 우 상단부터 0
d1 = [False] * 2 * N
# / 대각선을 체크하는 배열, 좌 상단부터 0
d2 = [False] * 2 * N


# 백트래킹
def backtracking(row) :

    global ans
    if row == N :
        ans += 1
        return
    
    for j in range(N if row else N // 2) :
        if not col[j] and not d1[row - j] and not d2[row + j] :
            col[j] = True
            d1[row - j] = True
            d2[row + j] = True

            backtracking(row + 1)

            #원상복귀
            d2[row + j] = False
            d1[row - j] = False
            col[j] = False


if N % 2 :
    # 홀수일 때, 첫번째 행에 퀸을 왼쪽 절반만 두고 경우의 수를 2배 취함 (정 가운데 제외)
    backtracking(0)
    ans *= 2

    # 첫번째 행을 정 가운데 뒀을 때의 경우의 수
    j = N // 2
    col[j] = d1[-j] = d2[j] = True
    backtracking(1)

    print(ans)

else :
    # 짝수일 때, 첫번째 행에 퀸을 왼쪽 절반만 두고 경우의 수를 2배 취함 (정 가운데 제외)
    backtracking(0)
    print(ans * 2)