# 자연수 N은 그보다 작거나 같은 제곱수들의 합
# 11의 제곱수 항의 최소 개수는 3개

# 7보다 작은 수부터 제곱수가 7보다 작은지 체크
# 작으면 7 - 제곱수

N = int(input())

number = N
ans = 0

while N != 0 :
    if number ** 2 > N :
        number -= 1
    else :
        N -= number ** 2
        ans += 1

    if N == 0 :
        print(ans)
        break