"""
백준 쉬운 최단거리(실버 1) :https://www.acmicpc.net/problem/14940

지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.


지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")

N , M = map(int,input().split())

grid =[list(map(int,input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

def bfs(grid, visited , start):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque([start])
    visited[start[0]][start[1]] = 0  # start의 값은 0이 맞잖아

    while queue:  # 큐가 빌때까지 하는거지
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:  # 이 범위일 때만
                if visited[nx][ny] == -1 and grid[nx][ny] == 1:  # visited이 아직 -1이고 grid에서 1이면
                    visited[nx][ny] = visited[x][y]+1  # 지금 visited배열에 현재 visited값에 1씩 더해줘야돼
                    queue.append((nx,ny))      # 여기를 잘못해줬아.................................. queue에 새로운 x,y좌표를 넣어줘야지 시발..

for i in range(N):
    for j in range(M):
        if grid[i][j] == 2: # 2인게 목표지점이니까 
            start = (i,j) # start 좌표 넘겨주고
        elif grid[i][j] == 0:  # 0이면 갈 수가 없으니까 
            visited[i][j] = 0  # visited 배열에 0으로 넣어줌

bfs(grid, visited , start)

for i in range(N):
    for j in range(M):
        print(visited[i][j],end=' ')
    print('')  # 2차원 배열 형태로 넣어주려면 이렇게 해야됌!!!
