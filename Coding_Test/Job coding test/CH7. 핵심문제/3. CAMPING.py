i = 0
L = 1
P = 1
V = 1

while (L != 0 and P != 0 and V != 0) :
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0 :
        break

    x = int(V // P)
    ans = int(V - ((P - L) * x))
    i += 1

    print("Case" + str(i) + " : " + str(ans))