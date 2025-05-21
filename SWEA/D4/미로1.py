import sys
sys.stdin = open("input.txt","r")

"""
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1

"""
from collections import deque
def bfs(start,end):
    visited = [[False]* 16 for _ in range(16)]

    queue = deque()
    queue.append(start)

    visited[start[0]][start[1]] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < 16 and 0<= ny < 16 and graph[nx][ny] in [0, 3] and not visited[nx][ny]:  # 여기에 도착점도 들어올 수 있게 해줘야됌.
                visited[nx][ny] = True
                queue.append((nx,ny))

    return visited[end[0]][end[1]]

for t in range(10):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start = (i,j)
            elif graph[i][j] == 3:
                end = (i,j)

    if bfs(start,end):
        print(f"#{N} 1")
    else:
        print(f"#{N} 0")