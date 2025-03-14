"""
백준 미로찾기(실버 2) : https://www.acmicpc.net/problem/2178

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
    queue= deque() # 방문해야 하는 queue


    visited = [[False for _ in range(M)] for _ in range(N)] # visited도 2차원 배열로 했었어야 되네....
    distance = [[1 for _ in range(M)] for _ in range(N)] # 거리를 넣어야할 2차원 배열


    # 시작 방문 노드를 0,0으로 해
    visited[0][0] = True


    #queue에 시작 위치를 넣어
    queue.append((0,0))

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
                print(distance)
        
            if visited[nx][ny] == True and nx == N-1 and ny == M-1:
                origin = distance[nx][ny]
                distance[nx][ny] = (distance[x][y]+1) if (distance[x][y]+1) < origin else origin

    return distance[N-1][M-1]  # 최종지점

    
print(bfs(grid,N,M))