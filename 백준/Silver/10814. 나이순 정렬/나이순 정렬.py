N = int(input())

result = []

for _ in range(N):
    inputs = list(input().split())

    peoples = [int(inputs[0]),inputs[1]]

    result.append(peoples)


for people in sorted(result,key=lambda x: x[0]):
    print(*people)