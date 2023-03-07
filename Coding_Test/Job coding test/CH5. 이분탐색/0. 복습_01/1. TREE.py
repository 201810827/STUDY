# 나무 M미터가 필요
# 절단기 높이 H
# 연속한 나무 길이를 자름
# H보다 긴 나무는 윗부분이 잘리고 잘린 나머지 부분을 갖고갈 수 있음

# 나무의 수 N, 필요한 나무의 길이 M
N, M = map(int, input().split())
# 나무들의 길이
tree = list(map(int, input().split()))

sorted(tree)

lo = 0
hi = tree[len(tree) - 1]
mid = (lo + hi) // 2

# 자른 나머지 나무의 합은 항상 M보다 크거나 작음
def cutter(h) :
    ts = 0
    
    for i in tree :
        if i > h :
            ts += i - h

    return ts

# 최대값 H
ans = 0
while lo <= hi :
    if cutter(mid) >= M :
        ans = mid
        lo = mid + 1
    else :
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)
