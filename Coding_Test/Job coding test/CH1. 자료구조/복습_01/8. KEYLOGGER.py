# 비밀번호 알아내기
# 대소문자, 숫자, 백스페이스, 화살표
from collections import deque

# 입력
N = int(input())
dq1 = deque()
dq2 = deque()

for _ in range(N) :
    sentence = input()
    for i in sentence :
        if i == '-' :
            if len(dq1) :
                dq1.pop()
        elif i == '<' :
            if len(dq1) :
                dq2.appendleft(dq1.pop())
        elif i == '>' :
            if len(dq2) : 
                dq1.append(dq2.popleft())
        else :
            dq1.append(i)

print(''.join(dq1) + ''.join(dq2))