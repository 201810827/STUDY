array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    # 왼쪽으로 순회
    for j in range(i, 0, -1) :
        if array[j] < array[j - 1] :
            array[j], array[j - 1] = array[j - 1], array[j]
        else :
            break

print(array)