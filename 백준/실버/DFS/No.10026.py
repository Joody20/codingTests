"""
백준 적록색약(골드 5): https://www.acmicpc.net/problem/10026

적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.


예제
5       ->   4 3
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

"""


import sys
sys.setrecursionlimit(10**6)  # Recursion Error 방지 (필요한 경우)
sys.stdin= open("input.txt", "r")

N = int(input())

grid=[list(map(str,input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

section_cnt = 0

def dfs(x,y,color,isRG):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not visited[nx][ny] and grid[nx][ny] == color and not isRG:  # 방문하지 않았고, grid에 있는 color랑 함수에서 받아온 color랑 같고, 적록색약이 아니면,
            dfs(nx,ny,color,isRG) # 원래대로 4구역으로 되는거고

        # 방문하지 않았고, color가 RG이고 grid에 있는 컬러에서 'RG'가 있거나 'B'가 있고, 적록색약이면 !!!
        elif not visited[nx][ny] and (color in 'RG' and grid[nx][ny] in 'RG' or color in 'B' and grid[nx][ny] in 'B') and isRG:
            dfs(nx,ny,color,isRG) # 3구역으로 나누는거야


def isRedGreen(isRG):  # 이 함수에 적록색약인지 아닌지를 구별하는 함수
    global visited

    visited=[[False]*N for _ in range(N)] # visited 배열을 다시 초기화 시켜

    section_cnt = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 방문하지 않았다면,
                dfs(i,j,grid[i][j],isRG) # 여기에 넘겨줘. 좌표값과 컬러랑 적록색약(True,False)
                section_cnt += 1

    return section_cnt

normal = isRedGreen(False) # 일반이면 False를 주고
weak = isRedGreen(True) # 적록색약이면 True를 줌

print(normal, weak)