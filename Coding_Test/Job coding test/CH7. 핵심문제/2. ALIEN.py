N, M = map(int, input().split())

stk = [[] for _ in range(7)]
cnt = 0

for _ in range(N) :

    melody, pret = map(int, input().split())
    
    # 프렛이 눌려져 있으면
    if pret in stk[melody] :
        # 현재 눌린 프렛이면 진행
        if stk[melody] and stk[melody][-1] == pret :
            continue 
        else :
            # 프렛보다 큰 프렛을 제거
            while stk[melody] and stk[melody][-1] > pret :
                stk[melody].pop()
                cnt += 1
    # 프렛이 눌려져있지 않으면
    else :
        # 프렛보다 큰 프렛을 제거한 후 
        while stk[melody] and stk[melody][-1] > pret :
            stk[melody].pop()
            cnt += 1
        # 새로운 프렛 삽입
        stk[melody].append(pret)
        cnt += 1


print(cnt)