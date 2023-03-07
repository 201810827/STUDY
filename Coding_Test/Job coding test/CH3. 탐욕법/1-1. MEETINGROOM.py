import sys

input = sys.stdin.readline

N = int(input())
meeting = []

for _ in range(N) :
    start, end = map(int, input().split())
    meeting.append((end, start))

meeting.sort()

time = 0
output = 0

for end, start in meeting :
    if time <= start :
        time = end
        output += 1

print(output)