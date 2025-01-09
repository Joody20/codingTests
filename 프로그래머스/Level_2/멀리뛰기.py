def solution(n):
    dp = [0] * (n+2)  # n = 1일 때 dp[2] = 2 라고 해놓은게 없기 때문에 런타임 에러가 나서 dp의 크기를 +2로 해줘야함.
    dp[1] = 1
    dp[2] = 2
    
    if n == 1:
        return 1 % 1234567
    
    elif n == 2:
        return 2 % 1234567
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567
    