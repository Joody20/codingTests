N = int(input())
N_array = list(map(int,input().split()))
M = int(input())
M_array = list(map(int,input().split()))


N_array.sort()

result = []

def parametric(target):
    start = 0
    end = N - 1


    while start <= end:
        mid = (start + end) // 2

        if target == N_array[mid]:
            return 1
        elif target > N_array[mid]:
            start = mid + 1
        elif target < N_array[mid]:
            end = mid - 1

    return 0


for i in M_array:
    result.append(parametric(i))

print(" ".join(map(str,result)))