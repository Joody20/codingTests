"""아래 그림과 같은 미로가 있다. 100*100 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

아래의 예시에서는 도달 가능하다.



[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")




def bfs(matrix, start , end):
    queue = deque([start])
    visited = [[0]*len(matrix) for _ in range(len(matrix[0]))]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while queue:
        x,y = queue.popleft()

        if (x,y) == end:
            return 1
        
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < len(matrix) and 0<=ny<len(matrix[0]) and matrix[nx][ny] != 1 and not visited[nx][ny]:
                queue.append((nx,ny))

    return 0


for _ in range(10):
    t = int(input())
    grid = [list(map(int,input())) for _ in range(100)]

    # sx,sy = 0,0
    # lx,ly = 0,0

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == 2:
                start = i,j
            elif grid[i][j] == 3:
                end = i,j

    print(f"#{t} {bfs(grid,start,end)}")


