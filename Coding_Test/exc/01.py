def solution(x, y, z) :
    k = 0
    for i in range(z) :
        if x - y >= z//2 or x > y :
            x = x + dx[0]
            k = max(x, k)
        else :
            x = x + dx[1]
            k += 1
            k = max(x, k)
    
    if x == y :
        return(k)
    else :
        return("-1")


x = int(input())
y = int(input())
z = int(input())

dx = [-1, 1]

print(solution(x, y, z))