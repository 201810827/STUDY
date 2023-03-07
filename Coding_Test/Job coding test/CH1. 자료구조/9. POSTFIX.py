N = int(input())
S = input()

# 피연산자만
alpha = []
# 후위표기식
postfix = []

for _ in range(N) :
    # 각 알파벳에 해당하는 숫자 입력받기
    alpha.append(int(input()))

for c in S :
    if c.isalpha() :
        postfix.append(alpha[ord(c) - ord('A')])
    else :
        i = postfix.pop()
        j = postfix.pop()
        if c == '+' :
            postfix.append(i+j)
        elif c == '-' :
            postfix.append(j-i)
        elif c == '*' :
            postfix.append(j*i)
        else :
            postfix.append(j/i)

print(f'{postfix[0]:.2f}')