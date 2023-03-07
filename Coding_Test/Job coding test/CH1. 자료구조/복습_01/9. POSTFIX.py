# 후위표기식 계산하기
import sys

# 입력
#input = sys.stdin.readline
# 피연산자 개수
N = int(input())
form = input()

# 피연산자만
arr = []
for _ in range(N) :
    arr.append(int(input()))
# 후위표기식
postfix = []

for i in form :
    if i.isalpha() :
        postfix.append(arr[ord(i) - ord('A')])
    else :
        a = postfix.pop()
        b = postfix.pop()
        if i == '+' :
            postfix.append(a+b)
        elif i == '-' :
            postfix.append(b-a)
        elif i == '*' :
            postfix.append(b*a)
        else :
            postfix.append(b/a)

print(f'{postfix[0]:.2f}')
