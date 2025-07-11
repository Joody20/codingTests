import sys
sys.stdin = open("input.txt","r")


"""
문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.


예제 1
3 15
1
5
12

출력 1
3

"""

n , k = map(int,input().split())
coins = [int(input()) for _ in range(n)]


dp = [float("inf")] * (k+1)  # 최소 개수를 구하는거니까 float("inf")를 해줘야됌.
dp[0] = 0  # k가 0일땐 항상 0이겟지!

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i - coin] + 1)  # 동전의 최소개수를 구하는 점화식


if dp[k] != float("inf"):
    print(dp[k])  # 가치의 합이 k인 경우의 동전의 최소 개수

else:
    print(-1)