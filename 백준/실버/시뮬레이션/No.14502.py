import sys
sys.stdin = open("input.txt","r")


"""
문제
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.



예제 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

출력 1
27

예제 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

출력 2
9

예제 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

출력 3
3

"""
from itertools import combinations
from collections import deque
import copy

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

# 빈칸과 바이러스 영역 좌표 저장
empty = []
virus = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:  # 0은 빈칸
            empty.append((i, j))
        elif maps[i][j] == 2:  # 2는 바이러스
            virus.append((i, j))


# BFS로 바이러스 퍼뜨리기
def virus_spread(temp_map):
    queue = deque(virus)  # 바이러스의 좌표를 deque로 queue에 저장해주고
    while queue:
        x,y, = queue.popleft()  # x,y 빼주고! 

        dx = [-1,0,1,0]  # 상하좌우 방향
        dy = [0,-1,0,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<=ny < M and temp_map[nx][ny] == 0:  # temp_map의 좌표가 빈칸이면
                temp_map[nx][ny] = 2  #  바이러스 퍼진거야.
                queue.append((nx,ny))   # 그 바이러스 퍼진 좌표 queue에 넣어주고... 아 대박

# 빈칸에서 벽 3개로 설치할 조합찾기
result = 0
for wall_comb in combinations(empty, 3):  # 빈칸 중 3개는 이제 벽이 되어야 하니까. combinations로 3개의 좌표를 조합해준거야.
    temp_map = copy.deepcopy(maps)

    for wx, wy in wall_comb:  # wall_comb는 벽을 세울 후보 3개의 좌표
        temp_map[wx][wy] = 1

    virus_spread(temp_map)  # 이제 그 temp_map에 바이러스를 퍼트리고!

    safe = sum(row.count(0) for row in temp_map) # 0을 세어서 더한걸 safe 변수에 저장
    result = max(result, safe)  # result와 safe의 최댓값을 구함.


print(result)








