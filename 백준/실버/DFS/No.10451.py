"""
백준 순열 사이클(실버 3) : https://www.acmicpc.net/problem/10451

예제
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8


"""

import sys
sys.stdin = open("input.txt","r")

T = int(input())

def dfs(graph, visited, v):
    visited[v] = 1  # 방문한건 1

    for i in graph[v]:  # 그래프에서 
        if not visited[i]:  # 방문하지 않은 건
            dfs(graph, visited, i) # 이 함수로 보내


for _ in range(1,T+1): 

    N = int(input())
    nums = list(map(int,input().split()))

    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(1,len(graph)):
        graph[i].append(nums[i-1])



    #사이클 찾기
    cnt = 0
    for i in range(1,len(graph)):
        if not visited[i]:
            dfs(graph,visited,i)
            cnt += 1

    print(cnt)