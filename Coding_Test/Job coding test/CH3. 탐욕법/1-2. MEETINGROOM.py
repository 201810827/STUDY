import sys

input = sys.stdin.readline
meeting = [tuple(map(int, input().split())) for _ in range(int(input()))]

meeting.sort(key = lambda x : (x[1], x[0]))

t = 0
ans = 0

for start, end in meeting :
    if t <= start :
        ans += 1
        t = end

print(ans)