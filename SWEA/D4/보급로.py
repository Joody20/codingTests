import sys
sys.stdin = open("input.txt","r")

"""
2차 세계 대전에서 연합군과 독일군의 전투가 점점 치열해지고 있다.

전투가 진행중인 지역은 대규모 폭격과 시가전 등으로 인해 도로 곳곳이 파손된 상태이다.

그림 1(a)에서와 같이 도로들은 전투로 인해 트럭이나 탱크와 같은 차량들이 지날 갈 수 없다.

전투에서 승리하기 위해서는 기갑사단과 보급부대가 신속하게 이동하기 위한 도로가 있어야 한다.

공병대는 출발지(S) 에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 한다.

도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.

출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.

출력 1
#1 2
#2 2
#3 8
#4 57
#5 151
#6 257
#7 18
#8 160
#9 414
#10 395

"""
from collections import deque
def bfs(start,finish):
    queue = deque()
    queue.append((start))

    min_cost = [[float("inf")] * N for _ in range(N)]
    min_cost[start[0]][start[1]]  = 0

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < N:
                next_time = min_cost[x][y] + graph[nx][ny]

                if next_time < min_cost[nx][ny]:
                    min_cost[nx][ny] = next_time
                    queue.append((nx,ny))

    return min_cost[finish[0]][finish[1]]

T = int(input())
for t in range(T):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(N)]

    start = (0,0)
    end = (N-1,N-1)

    print(f"#{t+1} {bfs(start,end)}")

    