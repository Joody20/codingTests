T = 10 #int(input())

for test_case in range(1, T + 1):
    case = int(input())
    que = list(map(int,input().split()))

    i=1
    while True:
        if i > 5:
            i = 1
            tmp = que.pop(0) - i
            if tmp <= 0:
                que.append(0)
                break
        que.append(tmp)
        i +=1


    print(f"#{case} ",*que)