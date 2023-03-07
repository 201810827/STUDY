from bisect import bisect_left, bisect_right

# 숫자카드 총 개수
N = int(input())
# 숫자카드의 숫자들
card = list(map(int, input().split()))
card.sort()

# 개수를 구할 숫자의 개수
M = int(input())
# 구해야 할 숫자들
target = list(map(int, input().split()))

ans = []
# 타겟의 위치와 타겟 +1의 위치값 구하기
for t in target :
    ans.append(bisect_right(card, t) - bisect_left(card, t))

print(' '.join(map(str, ans)))