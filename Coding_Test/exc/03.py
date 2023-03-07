box = list(map(int, input().split()))


i = 0
x = 0

while(box) :
    for j in range(len(box)) :
        if box[j] == max(box) :
            i = j
            break
        else :
            continue

    y = int(box[i] // 2)
    if y >= 1 and y <= box[i] :
            x = y
    
    box[i] = box[i] - x
    box[i - 1] = box[i - 1] + x

    if max(box) == min(box) :
         break
    else :
         continue

print(max(box))
