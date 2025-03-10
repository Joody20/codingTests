"""
백준 실버 2(자료구조 dfs) = https://www.acmicpc.net/problem/11724

예제
6 5
1 2
2 5
5 1
3 4
4 6

"""
import sys
sys.stdin = open("input.txt","r")


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u , v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


result = 0
visited = [False] * (N+1)

for i in range(1, N+1):
    if not visited[i]:
        dfs(graph , i, visited)
        result += 1

print(result)
  

