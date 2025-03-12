"""
백준 숫자고르기(골드 5) : https://www.acmicpc.net/problem/2668

예제
7
3
1
1
5
5
4
6

"""

import sys
sys.stdin=open("input.txt","r")

N = int(input())

graph = [[] * N for _ in range(N+1)]

result = []

def dfs(s,c):  # 시작 인덱스, 현재 인덱스의 값 1-> 3. 2-> 
    visited[s] = 1

    for i in graph[s]:
        if not visited[i]:
            dfs(i,c)
        elif visited[i] and i == c:  # 방문을 이미 했고, 사이클 도는 거
            result.append(i)  # result에 넣는거야

for i in range(1,N+1):  # 2줄의 그래프가 나오겟네 1234567 -> 3115546
    graph[int(input())].append(i)

for i in range(1,N+1): 
    visited = [0] * (N+1) # visited 배열 만들고
    dfs(i,i) # 같은 인덱스를 넘겨주면

print(len(result))
for i in result:
    print(i)

        
