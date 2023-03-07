from bisect import bisect_left, bisect_right

# 숫자카드 개수 N
N = int(input())
# 숫자카드에 적혀있는 정수 나열
card = list(map(int, input().split()))
card = sorted(card)

# 숫자카드에 적혀있는 정수의 개수 M
M = int(input())
# 찾고 싶은 정수의 나열
f_card = list(map(int, input().split()))

# 카드 개수 저장
cc = []

for i in f_card :
    cc.append(bisect_right(card, i) - bisect_left(card, i))

print(' '.join(map(str, cc)))