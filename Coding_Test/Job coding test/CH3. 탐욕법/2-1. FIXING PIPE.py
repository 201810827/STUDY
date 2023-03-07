N, L = map(int, input().split())

arr = []
for j in map(int, input().split()) :
    arr.append(j)

tape = 0
for k in range(0, N-1, 2) :
    if arr[k+1] - arr[k] <= L - 1 :
        tape += 1
    else :
        tape += 2

print(tape)