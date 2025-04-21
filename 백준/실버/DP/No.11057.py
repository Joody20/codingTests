"""
백준 오르막 수(실버 1) : https://www.acmicpc.net/problem/11057

오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.


첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.


"""

import sys
sys.stdin = open("input.txt","r")

N = int(input())

dp =[[0]* 10 for _ in range(N+1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2,N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1],dp[i-1][:j-1])

print(sum(dp[N]))