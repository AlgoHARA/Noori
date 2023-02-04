# 방 번호
# 구현에 관한 문제

# 필요한 세트 갯수 최소화 6, 9는 동일한 값
# 같은 값 = 갯수만큼 세트 필요 (예외 6,9)


arr = [0] * 10
n = map(int, input())
 
for i in range(len(n)) :
    num = int(n[i])
    if num == 6 or num == 9 :
        if arr[6] <= arr[9] :
            arr[6] += 1
        else :
            arr[9] += 1
    else :
        arr[num] += 1 

print(max(arr))
