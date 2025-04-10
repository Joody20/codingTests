"""
백준 골드 3 : 다리만들기  https://www.acmicpc.net/problem/2146

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

첫째 줄에 가장 짧은 다리의 길이를 출력한다.

즉, 1과 1 사이에 최소 0의 개수를 구하라는거야.

예제 1
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0

출력 1
3

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")

N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


# 섬의 개수를 알기 위한 bfs 함수
def bfs(x,y):
    global visited
    queue = deque()
    queue.append((x,y))

    visited[x][y] = True
    grid[x][y] = mark  

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<=ny <N and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    queue.append((nx,ny))
                    grid[nx][ny] = mark
                    visited[nx][ny] = True



def bfs2(island):
    queue = deque()
    dist = [[-1]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == island:
                queue.append((i,j))
                dist[i][j] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N:
                if grid[nx][ny] != island and grid[nx][ny] != 0:
                    return dist[x][y]
                
                if grid[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))


mark = 1 # 섬마다 부여하는 값

for x in range(N):
    for y in range(N):
        if grid[x][y] == 1 and not visited[x][y]:
            island_cnt = bfs(x,y)
            mark += 1

result = sys.maxsize
for i in range(1,mark):
    result=min(result, bfs2(i))

print(result)





    



