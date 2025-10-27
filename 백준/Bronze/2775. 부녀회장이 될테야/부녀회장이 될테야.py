T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    dp = [[0] * (N+1) for _ in range(K+1)]

    for i in range(1,N+1):
        dp[0][i] = i # 0층의 i호에는 i명이 산다.
        for k in range(1,K+1):
            dp[k][i] = dp[k-1][i] + dp[k][i-1]


    print(dp[K][N])
