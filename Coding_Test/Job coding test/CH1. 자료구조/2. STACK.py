# T개 데이터 입력받기
T = int(input())

for _ in range(T) :
    # 데이터 저장
    stk = []
    ans = 'YES'

    for c in input() :
        if c == '(' :
            stk.append(c)
        else :
            if len(stk) > 0 :
                stk.pop()
            else :
                ans = 'NO'

    if len(stk) > 0 :
        ans = 'NO'
        
    print(ans)