# Q. 손님에게 거슬러줘야하는 N원을 "최소한의 동전" 개수로 전해주기
# A. "가장 큰" 단위의 회폐 순서대로 거슬러주기

# 거슬러 줄 입력값 (n)
n = 1260

count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types :
    # 해당 coint으로 거슬러 줄 수 있는 동전 개수
    count += n // coin
    n %= coin

print(count)