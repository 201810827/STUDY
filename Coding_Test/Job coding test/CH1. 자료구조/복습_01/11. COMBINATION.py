# 합이 100이 되는 일곱 난쟁이 구하기
from itertools import combinations

arr = []

# 입력
for _ in range(9) :
    arr.append(int(input()))
    for i in combinations(arr, 7) :
        if sum(i) == 100 :
            for j in sorted(i) :
                print(j)
            break