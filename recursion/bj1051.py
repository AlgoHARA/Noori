# 1051번 - 숫자 정사각형
#  각 꼭짓점의 합이 최대가 되는 정사각형을 찾는 문제

n, m = map(int, input().split())

arr = []
for _ in range(n) :
            arr.append(list(map(int, input())))

ans = 1

# 모든 좌표를 탐색한다
for i in range(n) :
    for j in range(m) :
        # 50미만까지 
        for k in range(1, 50):
            # 두 가지를 모두 충족할 때
            if i + k < n and j + k < m :
                new = arr[i][j]

                if new == arr[i + k][j] and new == arr[i][j + k] and new == arr[i + k][j + k] :
                    # n x m 최대값 크기 출력
                    ans = max(ans, (k + 1) ** 2)

print(ans)
