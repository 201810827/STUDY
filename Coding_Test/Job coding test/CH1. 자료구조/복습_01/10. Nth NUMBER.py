# N*N의 배열에서 N번째 큰 수 찾기
import sys, heapq

# 입력
N = int(input())
hq = []

for _ in range(N) :
    for i in map(int, input().split()) :
        if len(hq) >= N :
            heapq.heappushpop(hq, i)
        else :
            heapq.heappush(hq, i)
    
print(heapq.heappop(hq))