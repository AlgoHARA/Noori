# 2501번 - 약수구하기

n, k = map(int, input().split())

arr = []
for i in range(1, n+1) :
    if n % i == 0 :
        # 배열에 값을 추가해준다
        arr.append(i)

if k > len(arr) :
    print(0)
else :
    print(arr[k-1])
