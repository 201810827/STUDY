# (KEY, VALUE)의 DICTIONARY 선언
books = dict()
N = int(input())

for _ in range(N) :
    name = input()

    if name in books :
        books[name] += 1
    else :
        books[name] = 1

# 가장 큰 값 찾기
max_val = max(books.values())

# 여러 개인 경우 생각
arr = []
for k, v in books.items() :
    if v == max_val :
        arr.append(k)

arr.sort()
print(arr[0])