# 2606번 - 바이러스

from collections import deque

# 컴퓨터 갯수
n = int(input())
# 연결선 갯수
v = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 방문 컴 표시
visited = [0] * (n + 1)
# 그래프 생성
for i in range(v) : 
    a, b = map(int, input().split())

    # a - b 간선 연결해주기
    graph[a] += [b]
    graph[b] += [a]

# 1번 컴퓨터부터 시작 - 방문표시를 해준다    
visited[1] = 1
que = deque([1])

while que :
    c = que.popleft()
    for k in graph[c] :
        if visited[k] == 0 :
            que.append(k)
            visited[k] = 1

print(sum(visited) - 1)
