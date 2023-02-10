# 1935번 - 후위 표기식2

import sys

n = int(input())
postfix = input()

# 대문자 값에 들어갈 숫자(피연산자)를 받는다
num = [int(input()) for i in range(n)]
stack = []

for i in postfix :
    if 'A' <= i <= 'Z' :
        # 후위표기식의 값이 알파벳이면, 스택에 값을 넣어준다. str -> int 형태로
        stack.append(num[ord(i) - ord('A')])

    else :
        # 숫자(피연산자)를 뽑아서 계산을 해준다
        op2 = stack.pop()
        op1 = stack.pop()

        if i == '+' :
            stack.append(op1 + op2)

        elif i == '-' :
            stack.append(op1 - op2)

        elif i == '/' :
            stack.append(op1 / op2)

        elif i == '*' :
            stack.append(op1 * op2)

# 소수점 3번째에서 반올림해서 2번째 자릿수까지만 출력하겠다.
print("{:.2f}".format(stack[0]))
