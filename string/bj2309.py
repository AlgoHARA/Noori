# 일곱난쟁이

N = map(int, input())
arr = [] 
for i in range(9):
    arr.append(int(input()))

arr.sort()    

total = sum(array)

for i in range(len(arr)):
    for j in range(i+1, len(arr)) :
        if total - (array[i] - array[j]) == 100 :
            for k in range(len(arr)) :
                if k == i or k == j :
                    pass
                else :
                    print(arr[k])
                exit()
