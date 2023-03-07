# 3개의 삼각수로 표현 가능한 자연수 찾기

T = [n * (n+1) // 2 for n in range(46)]

def triangular(n) :
    for i in range(1, 46) :
        for j in range(i, 46) :
            for k in range(j, 46) :
                if T[i] + T[j] + T[k] == n :
                    return 1
    return 0

for _ in range(int(input())) :
    print(triangular(int(input())))