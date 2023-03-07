# 배열 길이 N
N = int(input())

# N*N 배열
candy = []
for _ in range(N) :
    candy.append(list(input()))

ans = 1
# 빙고 탐색
def search() :
    # 글로벌 선언
    global ans
    # 행 탐색
    for i in range(N) :
        cnt = 1
        for j in range(1,N) :
            if candy[i][j-1] == candy[i][j] :
                cnt += 1
                # 연속된 부분의 값을 ans에 업데이트
                # 이전의 ans와 새로 센 연속 부분 cnt 중 더 긴 부분 저장
                ans = max(cnt, ans)
            else :
                # 다시 사용하기 위해 1 선언
                cnt = 1
    
    # 열 탐색
    for j in range(N) :
        cnt = 1
        for i in range(1,N) :
            if candy[i-1][j] == candy[i][j] :
                cnt += 1
                ans = max(cnt, ans)
            else :
                cnt = 1


# for 이중문 교환
for i in range(N) :
    for j in range(N) :
        # 인덱스 범위 주의
        # 행 교환 후 연속 부분 찾기
        if j + 1 < N :
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            # 탐색
            search()
            # 원상복구
            candy[i][j+1], candy[i][j] = candy[i][j], candy[i][j+1]
        # 열 교환 후 연속 부분 찾기
        if i + 1 < N :
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            search()
            candy[i+1][j], candy[i][j] = candy[i][j], candy[i+1][j]

# 가장 긴 연속 부분의 길이 출력
print(ans)