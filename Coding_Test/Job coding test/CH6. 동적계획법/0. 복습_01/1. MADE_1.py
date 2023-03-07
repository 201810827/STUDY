# TOP-DOWN
import sys
sys.setrecursionlimit(10 ** 6)
INF = 987654321

N = int(input())
# 연산횟수의 최소값을 저장할 배열
cache = [INF] * (N + 1)
cache[1] = 0

# N이 3으로 나누어지면 -> 3으로 나눈다
# N이 2로 나누어 떨어지면 -> 2로 나눈다
# 그 외의 경우 -> 1을 뺀다

def dp(x) :

    if cache[x] != INF :
        return cache[x]
    
    if x % 6 == 0 :
        cache[x] = min(dp(x // 3), dp(x // 2)) +  1
    elif x % 3 == 0 :
        cache[x] = min(dp(x // 3), dp(x - 1)) + 1
    elif x % 2 == 0 :
        cache[x] = min(dp(x // 2), dp(x - 1)) + 1
    else :
        cache[x] = dp(x - 1) + 1

    return cache[x]

print(dp(N))