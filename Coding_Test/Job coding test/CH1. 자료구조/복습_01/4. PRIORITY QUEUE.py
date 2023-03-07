# 1. 절대값이 가장 작은 값 출력
# 2. 그 값을 배열에서 제거
import sys, heapq

# 입력
# N개의 정수 x
input = sys.stdin.readlines
N = int(input())
hq = []

for _ in range(N) :
    x = int(input())
    for i in range(x) :
        if x == 0 :
            # x = 0 : 절대값이 가장 작은 값 출력 & 제거
            print(heapq.heappop(hq)[1] if len(hq) else 0)
        else :
            # x != 0 : 배열에 x 추가
            heapq.heappush(hq, (abs(x), x))