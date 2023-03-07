# 수열 A -> 수열 증가 부분 수열 중에서 합이 가장 큰 것

# 수열의 크기
N = int(input())
# 수열
A = list(map(int, input().split()))

dp = [0] * N
dp[0] = A[0]

for i in range(1, N) :
    for j in range(i) :
        if A[j] < A[i] :
            dp[i] = max(dp[i], dp[j])
    dp[i] += A[i]

print(max(dp))