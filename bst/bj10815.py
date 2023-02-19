# 10815번 - 숫자카드
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
search = list(map(int, sys.stdin.readline().split()))

# 카드 오름차순 정렬
card.sort()

def binary_search(array, data, left, right) :
    while left <= right :
        medium = (left + right) // 2
    
        # 각각의 요소들을 확인하는 문제
        if array[medium] == data:
            return medium
        # 중간 값보다 작다면, 중간보다 한칸 왼쪽 탐색
        elif array[medium] > data:
            right = medium - 1
        # 중간값보다 크다면 오른쪽 한 칸 앞 탐색
        else :
            left = medium + 1
    return None

for i in range(m) :
    if binary_search(card, search[i], 0, n - 1) is not None :
        print(1, end = ' ')
    else :
        print(0, end = ' ')
