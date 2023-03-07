# BOTTOM-UP
N = int(input())
DP = [0] * (N + 1)

for i in range(1, N + 1):

    DP[i] = i if i <= 2 else (DP[i - 1] + DP[i - 2]) % 10007

print(DP[N])