# 1158번 : 요세푸스 문제

from collections import deque

# 입력값을 나눠서 받아준다
n, k = map(int, input().split())

seat = deque()

for i in range(1, n+1) :
    seat.append(i)
    end = []

while seat :
    for i in range(k-1) :
        seat.append(seat.popleft())

    # 결과적으로 제거되는 순서 넣기    
    end.append(seat.popleft())

    
print(str(end).replace('[', '<').replace(']', '>'))
