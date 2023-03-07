n, M, K = map(int, input().split())
data = list(map(int, input().split()))

result = 0

data.sort()
first = data[n - 1]
second = data[n - 2]

count = (int(M / (K + 1)) * K) + M % (K + 1)

result += (count) * first
result += (M - count) * second

print(result)