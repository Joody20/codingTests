import sys
sys.stdin = open("input.txt","r")

"""
백준 가장 긴 바이토닉 부분 수열 : https://www.acmicpc.net/problem/11054

문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만, {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

예제 1
10
1 5 2 1 4 3 4 5 2 1

출력 1
7

"""
N = int(input())
nums = list(map(int,input().split()))

dp = [1] * 1001

# 앞에서부터 증가하는 부분수열 찾기
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

# 뒤집어서 증가하는 부분 수열 찾기
dp_back  = [1] * 1001

for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if nums[i] > nums[j]:
            dp_back[i] = max(dp_back[i], dp_back[j]+1)

# 구한 두 dp값들의 최대가 되는 값 구하기
answer = 0
for i in range(N):
    answer = max(answer, dp[i] + dp_back[i] - 1)

print(answer)