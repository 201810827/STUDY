# 1~N의 카드
# 1. 제일 위에 있는 카드 버리기
# 2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
# 3. 1~2 반복 후 제일 마지막에 남는 카드 구하기

from collections import deque

N = int(input())
dq = deque()

for i in range(1, N+1) :
    dq.append(i)

# 1개가 남아야하므로 1보다 커야함
while(len(dq) > 1) :
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())