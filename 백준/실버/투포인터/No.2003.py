import sys
sys.stdin = open("input.txt","r")

"""
백준 수들의합 2 : https://www.acmicpc.net/problem/2003

문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.


예제 1
4 2
1 1 1 1

출력 1
3

예제 2
10 5
1 2 3 4 2 5 3 1 1 2

출력 2
3

"""
n,m = map(int,input().split())
nums = list(map(int,input().split()))

result = 0
i = 0
j = 0
total = 0

while True:
    if total >= m:
        total -= nums[i]
        i += 1
    elif j == n:
        break
    else:
        total += nums[j]
        j += 1
    
    if total == m:
        result += 1

print(result)