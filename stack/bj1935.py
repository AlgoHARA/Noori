# 1935번 - 후위 표기식2

import sys

# 값을 받는다
n = int(sys.stdin.readline())

# 후위표기식 값을 받는다
postfix = sys.stdin.readline()

# 대문자 값에 들어갈 숫자(피연산자)를 받는다
num = [int(sys.stdin.readline()) for _ in range(n)]

# 갯수에 맞춰서 알파벳을 순서대로 넣어준다!
#stack = [int(sys.stdin.readline()) for _ in range(postfix)]

# stack에 값을 넣어주고, 값을 top부터 꺼내서 계산을 진행한다
stack = []

for i in postfix :
    if 'A' <= i <= 'Z' :
        # 후위표기식의 값이 알파벳이면, 스택에 값을 넣어준다. str -> int 형태로
        stack.append(num[ord(i) - 65])

    else :
        # 숫자(피연산자)를 뽑아서 계산을 해준다
        op1 = stack.pop()
        op2 = stack.pop()

        if i == '+' :
            #stack[op1 + op2]
            stack.append(op1 + op2)

        elif i == '-' :
            # stack[op2 - op1]
            stack.append(op2 - op1)

        elif i == '/' :
            # stack[op2 % op1]
            stack.append(op2 / op1)

        elif i == '*' :
            # stack[op2 * op1]
            stack.append(op2 * op1)

# 소수점 3번째에서 반올림해서 2번째 자릿수까지만 출력하겠다.
print("{:.2f}".stack[0])







