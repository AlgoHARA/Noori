# 11060번 - 점프점프

import sys

# 정수형태로 값을 받아와준다
num = int(sys.stdin.readline())

# 리스트 형태로 입력값을 담아준다
a = list(map(int, sys.stdin.readline().split()))

maze = [sys.maxsize] * (num + 1)
maze[0] = 0

# 반복문을 통해 점프 확인한다
for mazeNum in range(num) :
    # 재환이가 점프로 갈 수 있는 칸을 확인한다
    for jaewhan in range(a[mazeNum]) :
        if mazeNum + jaewhan + 1 < len(maze) :
            # 점프한 칸에 점프 횟수에 값을 최소값으로 초기화시켜준다
            maze[mazeNum + jaewhan + 1] = min(maze[mazeNum + jaewhan + 1], maze[mazeNum] + 1)

# 마지막 칸에 점프 횟수가 바뀌었다면 점프 횟수를 출력한다
if maze[num - 1] < sys.maxsize :
    print(maze[num - 1])
# 그것이 아니라면 -1을 출력한다
else :
    print(-1)
