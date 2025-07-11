import sys
sys.stdin = open("input.txt","r")


"""
인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2

M = 3이고, 바이러스를 아래와 같이 활성 상태로 변경한 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 비활성 바이러스는 *, 활성 바이러스는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.

* 6 5 4 - - 2
5 6 - 3 - 0 1
4 - - 2 - 1 2
3 - 2 1 2 2 3
2 2 1 0 1 - -
1 - 2 1 2 3 4
0 - 3 2 3 4 *
시간이 최소가 되는 방법은 아래와 같고, 4초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.

0 1 2 3 - - 2
1 2 - 3 - 0 1
2 - - 2 - 1 2
3 - 2 1 2 2 3
3 2 1 0 1 - -
4 - 2 1 2 3 4
* - 3 2 3 4 *

연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.

입력
첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 비활성 바이러스의 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

출력
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.


예제 1
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2

출력 1
4


"""
from itertools import combinations
from collections import deque

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]


# 바이러스를 활성화 시킬 수 있는 좌표들
virus_active = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            virus_active.append((i,j))


# 최소 시간 구할 시간들의 리스트
result = []

for virus_comb in combinations(virus_active, M):
    flag = True
    max_time = float("-inf")
    visited = [[-1] * N for _ in range(N)]


    for vx,vy in virus_comb:  # M개의 바이러스를 활성화 상태로 해줌.
        visited[vx][vy] = 0


    queue = deque(virus_comb)

    while queue:
        x,y = queue.popleft()

        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx< N and 0<= ny < N and visited[nx][ny] == -1:
                if maps[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))


    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:   # 빈칸만 처리해주는걸로 하는거야. 원래 연구소 2에서는 벽이 아니면 이제 최대 시간을 계산할 수 있게 했는데, 여기서는 벽이랑 비활성화 바이러스는 계산하면 안돼서 이렇게 빈칸인 경우에만 해주는걸로!!! 해주기만 하면됏엇음.
                if visited[i][j] == -1:
                    flag = False
                else:
                    max_time = max(max_time, visited[i][j])


    if not flag:
        continue
    else:
        result.append(max_time)


if len(result) == 0:
    print(-1)
else:
    result = min(result)
    if result != float("-inf"):  # result가 -inf인 경우도 있었어서 그때는 0으로 리턴하게끔 경우처리 해줌.
        print(result)
    else:
        print(0)
