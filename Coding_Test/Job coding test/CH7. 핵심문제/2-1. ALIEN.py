import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = 0
stk = [[] for _ in range(7)]

for _ in range(N) :

    melody, pret = map(int, input().split())

    while stk[melody] and stk[melody][-1] > pret :
        stk[melody].pop()
        cnt += 1

    if stk[melody] and stk[melody][-1] == pret :
        continue

    stk[melody].append(pret)
    cnt += 1

print(cnt)