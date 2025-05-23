import sys
sys.stdin = open("input.txt","r")

"""
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.


3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 5
#2 5
#3 0



"""
from collections import deque
def bfs(start,end):
    visited = [[-1]*(N+1) for _ in range(N+1)]  # 미로의 거리를 구하는 거니까! -1로 해주기!!
    queue = deque()
    queue.append(start)

    visited[start[0]][start[1]] = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N:
                if graph[nx][ny] in [0,3] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

    return visited[end[0]][end[1]] - 1

T=int(input())

for t in range(T):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                start = (i,j)
            elif graph[i][j] == 3:
                end = (i,j)
    result = bfs(start, end)
    if result > 0:
        print(f"#{t+1} {result}")
    else:
        print(f"#{t+1} 0")