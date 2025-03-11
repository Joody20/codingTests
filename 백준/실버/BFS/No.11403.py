"""
백준 경로찾기(실버 1): https://www.acmicpc.net/problem/11403

예제 1
3
0 1 0 
0 0 1
1 0 0

예제 2
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0

"""
import sys
sys.stdin = open("input.txt","r")

N = int(input())

graph = [[] * N for _ in range(N)] # 가중치 없는 2차원 배열 그래프 

for i in range(N):
    S = list(map(int,input().split()))  # 리스트 형태로 각 행을 받아와 
    for j in range(N):
        if S[j] == 1: # S의 배열 중 요소 중에 1인거면 
            graph[i].append(j) # graph[i]에 j를 넣어

result = [[0] * N for _ in range(N)] # 결과를 나타낼 2차원 배열

def bfs(start):
    visited = [0] * N # 방문 했는지를 알기 위함.
    queue = []
    queue.append(start)

    while queue: # 큐가 비어질 때 동안
        cur = queue.pop(0) # 첫번 째 요소를 빼
        for next in graph[cur]: # graph 현재 노드를 빼
            if visited[next] == 0: # 방문하지 않았다면, 
                visited[next] = 1 # 방문 했다고 1로 표시
                result[start][next] = 1 # result배열에도 (i,j)에 1을 넣는거야
                queue.append(next) # queue에 다음거를 넣고

    
for i in range(N):
    bfs(i)

for i in range(N):
    for j in range(N):
        if j == N-1: # 이게 맨 마지막 까지 되면,
            print(result[i][j]) # result 배열을 출력함.
        else:
            print(result[i][j], end=' ')




