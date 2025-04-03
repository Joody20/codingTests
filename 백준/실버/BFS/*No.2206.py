"""
백준 벽부수고 이동하기(골드 3): https://www.acmicpc.net/problem/2206

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.


첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.


첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 1
6 4
0100
1110
1000
0000
0111
0000

출력 1
15

예제 2
4 4
0111
1111
1111
1110

출력 2
-1

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")

N , M = map(int,input().split()) # N이 세로, M이 가로

maps = [list(map(int,input().strip())) for _ in range(N)]  # maps임

visited = [[[0,0] for _ in range(M)] for _ in range(N)]

result = 0 # 최단경로를 세는 거

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):
    queue = deque([(x,y,0)]) # x,y좌표와 벽 부수는 횟수
    visited[y][x][0] = 1   # 방문처리


    while queue:
        x, y, break_cnt = queue.popleft()

        if (x,y) == (M-1,N-1):    # 최종 지점에 다다르면
            return visited[y][x][break_cnt]  # 그때의 x,y,벽부순횟수까지의 수
        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < M and  0 <= ny < N:  # 가로 세로
                if maps[ny][nx] == 1 and break_cnt == 0:  # 벽인 경우 벽을 부순다.  벽 한번밖에 못부시니까 break_cnt가 0일 때,
                    visited[ny][nx][1] = visited[y][x][0] + 1 # 벽 한번 부시고
                    queue.append([nx,ny,1])  # 벽 부순 횟수 queue에 넣어주기

                if maps[ny][nx] == 0 and visited[ny][nx][break_cnt] == 0:
                    visited[ny][nx][break_cnt] = visited[y][x][break_cnt] + 1 # 이거 방문처리 하고 지금까지 온 횟수 세야하니까 1 더해주는거야
                    queue.append([nx,ny,break_cnt])


    return -1

print(bfs(0,0))
print(visited)


