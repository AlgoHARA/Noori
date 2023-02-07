# 2164번 : 카드2

# 제일 마지막으로 남게 되는 카드를 구해라
# 1. 제일 위에 있는 카드를 바닥에 버린다. 
# 2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 1234 -> 234 -> 342 -> 42 -> 24 -> 4

from collections import deque

num = int(input())

# 새로운 큐 생성한다
queue = deque()

for i in range(1, num + 1):
    # 큐에 값을 넣어준다
    queue.append(i)
 
while(len(queue) != 1):
    # 맨 윗쪽 카드 버려라
    queue.popleft()
    # 맨 윗쪽 카드 제일 아래로 옮겨라!
    queue.append(queue.popleft()) 
 
print(queue[0])
