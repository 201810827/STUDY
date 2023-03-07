# 올바른 VPS 찾기

# 입력
# T개의 테스트 데이터와 문자열
T = int(input())

for _ in range(T) :
    vps = input()
    # 문자열 저장 스택
    stk = []
    # 출력
    # YES or NO
    ans = 'YES'
    
    for i in (vps) :
        if i == '(' :
            stk.append(i)
        else :
            if len(stk) > 0 :
                stk.pop()
            else :
                ans = 'NO'
    
    if len(stk) > 0 :
        ans = 'NO'
    
    print(ans)