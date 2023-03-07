# 1~N까지의 사람, K번째 사람을 계속해서 제거해감

# 입력
# N과 K가 빈칸을 사이에 두고 순서대로 주어짐
N, K = map(int, input().split())
array = [i for i in range(1, N+1)]
# 출력 번째
cnt = 0
# 출력된 순서
ans = []

for _ in range(N) :
    # array의 K번째 (배열은 0부터 시작)
    cnt += K - 1
    # K가 array의 길이보다 큰 경우
    cnt %= len(array)
    # array에서 제거 -> ans에 삽입
    ans.append(array.pop(cnt))

print(f"<{', '.join(map(str,ans))}>")