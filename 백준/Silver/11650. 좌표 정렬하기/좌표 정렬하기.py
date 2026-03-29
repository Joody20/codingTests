N = int(input())

result = []

for i in range(N):
    coordinates = list(map(int,input().split()))

    result.append(coordinates)

    # x좌표가 같으면,,, y좌표 증가순으로...................................

sorted_list = sorted(result, key= lambda x : (x[0],x[1]))


for lst in sorted_list:
    print(*lst)