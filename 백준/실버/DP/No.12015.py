import sys
sys.stdin = open("input.txt","r")

"""
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 1
6
10 20 10 30 20 50

출력 1
4

"""
import bisect

N = int(input())
arr = list(map(int,input().split()))

dp = []
for i in arr:
    idx = bisect.bisect_left(dp,i)  # i가 들어갈 dp에서의 가장 왼쪽 위치

    if idx == len(dp):  # idx가 첫번째면 dp의 길이가 0이어야 그 위치에 삽입, idx가 두번째면 dp의 길이가 1이여야 인덱스1번에 삽입 ,,, 반복
        dp.append(i)
    else:  # 그 위치에 넣을 수 없다면! dp[idx] = i로 update를 해줘야함! 그래야 dp에 정확한 위치에 값이 들어갈 수 있음.
        dp[idx] = i

# print(dp)
print(len(dp))

