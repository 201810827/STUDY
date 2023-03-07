# 현재 회사에 출근한 사람 구하기

import sys

# 입력
input = sys.stdin.readline
N = int(input())
check = set()

for _ in range(N) :
    name, el = input().split()
    if el == 'enter' :
        check.add(name)
    else :
        if name in check :
            check.remove(name)

for name in sorted(check, reverse = True) :
    print(name)