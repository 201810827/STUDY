# Q. N이 1이 될때까지 다음을 반복
# (1) N에서 1을 뺀다
# (2) N를 K로 나눈다 (나누어 떨어질 때만)

N, K = map(int, input().split())
count = 0

while(N >= K) :
    # 나누어 떨어지지 않으면 N - 1
    while N % K != 0 :
        N -= 1
        count += 1
    N /= K
    count += 1

while(N > 1) :
    N -= 1
    count += 1

print(count)
