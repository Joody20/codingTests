import sys
sys.stdin = open("input.txt","r")

T = int(input())

for _ in range(1,T+1):
    #금광 정보 입력
    N , M = map(int,input().split())
    array = list(map(int,input().split()))

    # dp 테이블 초기화
    dp = []
    index = 0

    for i in range(N):
        dp.append(array[index:index+M])  # M단위로 슬라이싱해서 dp테이블에 넣는거야.
        index += M

    #bottom-up 방식의 다이나믹 프로그래밍
    for j in range(1, M): #열 기준
        for i in range(N): # 행 기준
            #왼쪽 위에서 오는 경우
            if i == 0:          # 인덱스를 벗어나지 않는지 체크하기 위함임
                leftup = 0
            else:
                leftup = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == N - 1:      # 인덱스를 벗어나지 않는지 체크하기 위함임
                leftdown = 0
            else:
                leftdown = dp[i+1][j-1]
            # 왼쪽에서 오는 경우   
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(leftup, leftdown , left)

    result = 0
    for i in range(N):
        result = max(result , dp[i][M-1])
    print(result)
