# N개의 테스트 케이스
N = int(input())

# 1000까지의 삼각수 배열
T= []
for n in range(46) :
    T.append(int(n*(n+1)//2))

# 3중 for문으로 3개의 삼각수 조합 구하기
def is_possible(K) :
    for i in range(1, 46) :
        for j in range(i, 46) :
            for k in range(j, 46) :
                if T[i] + T[j] + T[k] == K :
                    return 1
    return 0

for _ in range(N) :
    print(is_possible(int(input())))