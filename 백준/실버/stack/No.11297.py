"""
백준 실버 2(자료구조) 최대힙: https://www.acmicpc.net/problem/11297

예제
13
0
1
2
0
0
3
2
1
0
0
0
0
0

"""

import heapq
import sys 
sys.stdin = open("input.txt" , "r")


N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(N)]

h = []

for n in numbers:
    if n == 0:
        if h:
            maxx = -heapq.heappop(h) # 리턴할 때는 -를 붙혀서 리턴해줌.. ㄹㅈㄷ,,,,
            print(maxx)
        else:
            print(0)

    else:
        heapq.heappush(h, -n)  # push할 때 음수로 push 하고