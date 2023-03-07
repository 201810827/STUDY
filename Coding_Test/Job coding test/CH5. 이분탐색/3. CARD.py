# 카드 개수
N = int(input())

# 카드 숫자들 개수 세기
card = {}
for i in map(int, input().split()) :
    if i in card :
        card[i] += 1
    else :
        card[i] = 1

M = int(input())

# 타겟의 개수 찾기
ans = []
for i in map(int, input().split()) :
    if i in card :
        ans.append(card[i])
    else :
        ans.append(0)
        
print(' '.join(map(str, ans)))