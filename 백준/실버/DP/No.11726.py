"""
백준 2xn 타일링 : https://www.acmicpc.net/problem/11726

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)  -> 그래서 dp의 크기를 1001로 해줘야됌.

첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

"""

import sys
sys.stdin = open("input.txt","r")

N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3 , N+1):
    dp[i] = (dp[i-1]+dp[i-2]) % 10007

print(dp[N])

