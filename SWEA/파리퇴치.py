T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]  # 2차원 배열

    result = 0

    for i in range(N - M + 1):  # 영역? 5 - 2 + 1 = 4 까지인거야
        for j in range(N - M + 1):  # 4 까지인거야 

            current_sum= 0

            for k in range(M): # M = 2까지
                for l in range(M): # M = 2까지
                    current_sum += lst[i+k][j+l]   # []
    
            result = max(result, current_sum)

    print(f"#{tc} {result}")