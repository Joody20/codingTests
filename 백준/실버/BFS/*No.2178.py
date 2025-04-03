"""
백준 미로찾기(실버 2) : https://www.acmicpc.net/problem/2178

N×M크기의 배열로 표현되는 미로가 있다.

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제
4 6
101111
101010
101011
111011

"""
from collections import deque
import sys
sys.stdin = open("input.txt", "r")

N , M = map(int,input().split())

grid=[list(map(int,input())) for _ in range(N)]


def bfs(matrix,x,y):
    queue= deque([(0,0)]) # 방문해야 하는 queue에 시작위치를 넣어, 이 때 [(0,0)] 이런식으로 꼭 넣어줘야돼.
 
    visited = [[False for _ in range(M)] for _ in range(N)] # visited도 2차원 배열로 했었어야 되네....
    distance = [[1 for _ in range(M)] for _ in range(N)] # 거리를 넣어야할 2차원 배열

    # 시작 방문 노드를 0,0으로 해
    visited[0][0] = True


    dx = [0,1,0,-1]
    dy = [1, 0 , -1,0]


    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == False and matrix[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                distance[nx][ny] += distance[x][y]
                # print(distance)
        
            if visited[nx][ny] == True and nx == N-1 and ny == M-1:
                origin = distance[nx][ny]
                distance[nx][ny] = (distance[x][y]+1) if (distance[x][y]+1) < origin else origin
                
    print(distance)
    return distance[N-1][M-1]  # 최종지점

print(bfs(grid,N,M))
