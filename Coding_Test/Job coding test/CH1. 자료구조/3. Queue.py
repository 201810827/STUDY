from collections import deque

N = int(input())

dq = deque()
for i in range(1, N + 1) :
    # FIFO 삽입
    dq.append(i)

while(len(dq) > 1) :
    # FIFO 삭제
    dq.popleft()
    # FIFO 삭제
    j = dq.popleft()
    # FIFO 삽입
    dq.append(j)

print(dq.pop())
