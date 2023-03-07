n = int(input())
cost = list(map(int, input().split()))
x = int(input())

result = 0

cost.sort()

for i in range(len(cost) - 1, 0, -1) :
    if x >= cost[i] :
        x = x - cost[i]
        result += 2 ** i

print(result)