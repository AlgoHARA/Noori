# 1388번 - 바닥 장식

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

floor = []


# 행렬 받기
for _ in range(n) : 
    floor.append(list(input()))

count = 0

# '-' 탐색
for i in range(n) :
    pre = "/"
    for j in range(m) :
        if floor[i][j] == "-" :
            if floor[i][j] != pre : count += 1
        pre = floor[i][j]

# '|' 탐색
for j in range(m) :
    pre = "/"
    for i in range(n) :
        if floor[i][j] == "|" :
            if floor[i][j] != pre : count += 1
        pre = floor[i][j]

# 갯수 출력
print(count)
