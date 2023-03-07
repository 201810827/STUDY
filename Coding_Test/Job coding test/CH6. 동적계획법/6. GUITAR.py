# 레슨의 수, 블루레이의 수
N, M = map(int, input().split())
# 각 레슨의 길이
lesson = list(map(int, input().split()))

low = lesson[0]
high = lesson[len(lesson) - 1]
mid = (low + high) // 2

sum1 = 0
sum2 = 0
ans = 0

for _ in range(M - 1) :
    for i in range(len(lesson)) :
        if (lesson[i] <= mid) :
            sum1 += lesson[i]
        else :
            sum2 += lesson[i]

    if sum1 < sum2 :
        low = mid + 1
    elif sum1 == sum2 :
        break
    else :
        high = mid - 1 

    mid = (low + high) // 2
    ans = max(sum1, sum2)

print(ans)