# TOP-DOWN
N = int(input())
cache = [0] * (N + 1)

def tile(x) :

    if cache[x] != 0 :
        return cache[x]
    
    cache[x] = x if x <= 2 else (tile(x - 1) + tile(x - 2)) % 10007

    return cache[x]

print(tile(N))