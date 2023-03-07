import sys, heapq

N = int(input())
hq = []

for _ in range(N) :
    for i in map(int, input().split()) :
        if len(hq) >= N : 
            heapq.heappushpop(hq, i)
        else :
            heapq.heappush(hq, i)
    
    print(hq)

print(heapq.heappop(hq))