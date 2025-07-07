import sys
sys.stdin = open("input.txt","r")


"""
문제
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

입력
첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

출력
첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 1
20 2
출력 1
21

"""

N, K = map(int,input().split())
MOD = 1000000000

dp = [[0]*(K+1) for _ in range(N+1)]

dp[0][0] = 1
dp[0][K] = 0

#숫자 n을 1개로 만드는 경우는 1
for i in range(N+1):
    dp[i][1] = 1

for k in range(2,K+1): # 2개부터 K개까지
    for n in range(N+1): # 0부터 n까지
        for i in range(n+1):  #마지막에 더한 수 i? -> 여기가 이해가안가..
            dp[n][k] = (dp[n][k] + dp[n-i][k-1]) % MOD

print(dp[N][K])


