"""
백준 실버 2 가장 큰 증가하는 부분수열 : https://www.acmicpc.net/problem/11055


수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가하는 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.


첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)



첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.


예제 1
10
1 100 2 50 60 3 5 6 7 8

출력 1
113

"""
import sys
sys.stdin = open("input.txt","r")


N = int(input())
nums = list(map(int,input().split()))

dp  = [1] * 1001

dp[0] = nums[0]   # 이거 해주기이이이

for i in range(1,N):
    for j in range(0,i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i] , dp[j] + nums[i])   # 여기서 nums안에 있는 숫자를 더해줘야돼. 그 더한 숫자가 가장 큰
        else:
            dp[i] = max(dp[i] , nums[i])  # 감소하는거라면 그래도 일단 둘중에 더 큰 값을 넣어줌.

print(max(dp))