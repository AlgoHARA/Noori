# 17608번 - 막대기

import sys
n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(n)]
before = stack.pop()
count = 1

for i in range(1, n) :
    last = stack.pop()
    if last > before :
        count += 1
        before = last

print(count)


