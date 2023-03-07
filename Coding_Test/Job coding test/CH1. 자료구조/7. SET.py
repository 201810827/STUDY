import sys

input = sys.stdin.readlines
n = int(input())

person = set()
for _ in range(n) :
    name, el = input().split()

    if el == 'enter' :
        person.add(name)
    else :
        if name in person :
            person.remove(name)

for name in sorted(person, reverse = True) :
    print(name)
