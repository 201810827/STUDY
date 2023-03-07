# 나무의 수 N, 필요한 나무 M
N, M = map(int, input().split())
# 나무 길이 배열
tree = list(map(int, input().split()))
tree.sort()

# 최대값
high_ans = 0

left = tree[0]
right = tree[len(tree) - 1]
mid = (left + right) // 2

# 절단기
def tree_cutting(h) :

    total = 0
    for t in tree :
        if t > h :
            total += (t - h)

    return total

while left <= right :

    if tree_cutting(mid) >= M :
        high_ans = mid
        left = mid + 1
    else :
        right = mid - 1

    mid = (left + right) // 2

print(high_ans)