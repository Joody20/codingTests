N = int(input())
arrays = list(map(int,input().split()))


empty = []

empty.append(arrays[0])

for i in range(1,N):
    if empty[-1] < arrays[i]:
        empty.append(arrays[i])
    else:
        break


if(len(empty) == N):
    print("1")
else:
    print("0")