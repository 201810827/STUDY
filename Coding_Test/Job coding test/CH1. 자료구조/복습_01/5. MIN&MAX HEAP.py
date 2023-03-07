# 양수 : min_heap 저장
# 음수 : max_heap 저장

import sys, heapq

input = sys.stdin.readline

# N개의 연산정보 정수 x
N = int(input())
min_heap = []
max_heap = []

for _ in range(N) :
    x = int(input())
    if x == 0 :
        if len(min_heap) :
            if len(max_heap) == 0 or min_heap[0] < max_heap[0] :
                print(heapq.heappop(min_heap))
            else :
                print(-heapq.heappop(max_heap))
        else :
            print(-heapq.heappop(max_heap) if len(max_heap) else 0)
    elif x > 0 :
        heapq.heappush(min_heap, x)
    else :
        heapq.heappush(max_heap, -x)
