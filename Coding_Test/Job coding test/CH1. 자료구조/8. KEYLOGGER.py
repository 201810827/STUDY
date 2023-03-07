from collections import deque

N = int(input())
d1 = deque()
d2 = deque()

for _ in range(N) :
    case = input()

    for c in (case) :
        if c == '-' :
            if len(d1) :
                d1.pop()
        elif c == '<' :
            if len(d1) :
                d2.appendleft(d1.pop())
        elif c == '>' :
            if len(d2) :
                d1.append(d2.popleft())
        else :
            d1.append(c)

print(''.join(d1) + ''.join(d2))