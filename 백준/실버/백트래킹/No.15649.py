"""
백준 N과 M(1) : https://www.acmicpc.net/problem/15649

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.


예제 1
3 1

출력 1
1
2
3

예제 2
4 2

출력 2
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3

"""
from itertools import permutations
import sys
sys.stdin = open("input.txt","r")

N,M = map(int,input().split())

res = []

for i in range(1,N+1):
    res.append(i)

result = list(permutations(res,M))

for r in result:
    for i in r:
        print(i,end=' ')
    print()
    
