"""
동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출 해야 합니다.
동빈이의 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
이 때 괴물이 있는 부분은 0 으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출 할 수 있는 형태로 제시됩니다.
이 때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작칸과 마지막 칸을 모두 포함해서 계산합니다.

예제
5 6
101010
111111
000001
111111
111111

"""

from collections import deque
import sys
sys.stdin = open("input.txt","r")

N , M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

# 이동할 상하좌우 방향 정의

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0: # 벽이 있는 경우 무시
                continue
            # 해당 경로를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[N-1][M-1] # 가장 오른쪽 아래 마지막까지의 최단 거리 반환

print(bfs(0,0))
