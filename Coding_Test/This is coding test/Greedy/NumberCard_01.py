# n, m 자연수를 공백으로 구분
n, m = map(int, input().split())

# n*m 행의 카드 행렬을 "한 줄씩"
result = 0

for i in range(m) :
    data = list(map(int, input().split()))
    min_value = min(data)
    # result를 큰 수로 업데이트
    result = max(result, min_value)

print(result)