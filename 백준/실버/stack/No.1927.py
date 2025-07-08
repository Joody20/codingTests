"""
백준 실버 2(자료구조) 최소힙: https://www.acmicpc.net/problem/1927

예제
9
0
12345678
1
2
0
0
0
0
32

"""
import heapq
import sys
sys.stdin = open("input.txt" , "r")


N = int(input().rstrip())  # N개의 수

numbers = [int(input().rstrip()) for _ in range(N)]

res = []

for n in numbers:
    if n == 0:
        if res: # 배열이면,
           minn = heapq.heappop(res)  # heapqpop를 쓰면 자동으로 최소값을 빼줌.
           print(minn)
        else: # 배열이 비어 있으면 
           print('0') # 0을 출력

    else: # n이 0이 아니면
        heapq.heappush(res, n) # res 배열에 n을 push 해줌.


"""
도저히 무슨 방법을 해도 계속 시간초과 였는데 내가 다른 점이라곤 sys.stdin.readline()을 인했다는 점...;;;;

import sys
import heapq 

N = int(sys.stdin.readline())
heap=[]

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
"""
