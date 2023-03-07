# 가장 많이 팔린 책의 제목 출력하기

# 입력
N = int(input())
book = dict()

for _ in range(N) :
    name = input()

    if name in book :
        book[name] += 1
    else :
        book[name] = 1
    
max_book = max(book.values())
arr = []
for k, v in book.items() :
    if v == max_book :
        arr.append(k)

arr.sort()
print(arr[0])