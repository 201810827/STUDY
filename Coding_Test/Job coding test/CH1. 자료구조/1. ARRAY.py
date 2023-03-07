# 1 <= K <= N <= 1000

N, K = map(int, input().split())

array = [i for i in range(1, N+1)]
pt = 0
ans = []

for _ in range(N) :
    pt += K - 1
    pt %= len(array)
    ans.append(array.pop(pt))


print(f"<{', '.join(map(str, ans))}>")