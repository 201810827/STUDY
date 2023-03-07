n = map(int, input().split())
box = list(map(int, input().split()))


i = 0
x = 0


result = max(box)
for j in range(len(box)) :
    if result == box[j] and j >= 2 and j <= len(box) :
        i = j
        break

result2 = 0
result3 = 0
for j in range(i, 0, -1) :
    result2 = box[j] - box[j - 1]
    result3 = max(result2, x)
    if result3 >= 1 and result3 <= box[i] :
        x = result3
    else :
        continue

box[i] = box[i] - x
box[i - 1] = box[i - 1] + x

print(box)