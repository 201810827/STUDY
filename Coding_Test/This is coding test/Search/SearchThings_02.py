def binary_search(array, target, start, end) :
    while start <= end :
        mid = int((start + end) // 2)
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return None
    
n = int(input())
number1 = list(map(int, input().split()))
number1.sort()

m = int(input())
number2 = list(map(int, input().split()))

for i in number2 :
    result = binary_search(number1, i, 0, n - 1)
    if result != None :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')
