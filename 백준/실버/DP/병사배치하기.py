import sys
sys.stdin = open("input.txt", "r")

N = int(input())

array = list(map(int,input().split()))
array.reverse()

dp = [1] * N

for i in range(1,N):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(N - max(dp))

