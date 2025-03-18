"""
백준 돌게임(실버 5) : https://www.acmicpc.net/problem/9655

돌 게임은 두 명이서 즐기는 재밌는 게임이다.

탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.

두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.

첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)

상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.

"""

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
res = 0

d = [-1] * 10001

d[1] = 1 # SK
d[2] = 0  # CY
d[3] = 1 # SK


for i in range(4,N+1):
    if d[i-1] == 1 or d[i-3] == 1:
        d[i] = 0
    else:
        d[i] = 1

if d[N] == 1:
    print('SK')
else:
    print('CY')