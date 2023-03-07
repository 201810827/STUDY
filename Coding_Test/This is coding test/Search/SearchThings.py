n = int(input())
number1 = list(map(int, input().split()))

m = int(input())
number2 = list(map(int, input().split()))

for i in number2 :
    if i in number1 :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')