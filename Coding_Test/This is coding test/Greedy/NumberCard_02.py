n, m = map(int, input().split())
result = 0

# 이중 반복문
for i in range(m) :
    data = list(map(int, input().split()))
    min_value = 10001
    
    for j in data :
        min_value = min(min_value, j)
    
    result = max(result, min_value)

print(result)