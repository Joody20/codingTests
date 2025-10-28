N = int(input())
N_array = sorted(list(map(int,input().split())))
M = int(input())
M_array = list(map(int,input().split()))

  

dic = {}
for i in N_array:
    if i in dic:
        dic[i] += 1 # N_array 안에 있는 값이 있으면 그 값의 횟수 저장해줌. 즉, 몇 번 나왔는지..
    else:
        dic[i] = 1

# print(dic)


def parametric(target):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end ) // 2

        if target == N_array[mid]:
            return dic[target]
        elif target < N_array[mid]:
            end = mid - 1
        elif target > N_array[mid]:
            start = mid + 1

result = []
for i in M_array:
    if parametric(i):
        result.append(dic[i])
    else:
        result.append(0)

print(" ".join(map(str,result)))