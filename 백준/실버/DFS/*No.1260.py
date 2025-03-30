"""
백준 DFS와 BFS (실버 2) : https://www.acmicpc.net/problem/1260

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

"""

from collections import deque
import sys
sys.stdin = open("input.txt","r")

N , M , V = map(int,input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

visited = [False] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = " ")
    for n in range(1,N+1):
        if not visited[n] and graph[idx][n]:
            dfs(n)

def bfs(v):
    global visited
    queue = deque([v]) # deque([v])
    visited[v] = True  # 여기에 방문 표시 꼭 해줘야돼 !!!!!!!!!!!!
    
    while queue:
        cur = queue.popleft()
        print(cur, end = " ")
        for n in range(1, N+1):
            if not visited[n] and graph[cur][n]:
                visited[n] = True  # 여기서도 방문표시 !!!
                queue.append(n)
                

dfs(V)
print()
visited = [False] * (N+1)  # DFS 후에 BFS 출력하려면 visited 배열 초기화 해줘야 함.
bfs(V)
print()