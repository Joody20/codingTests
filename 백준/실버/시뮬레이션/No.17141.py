import sys
sys.stdin = open("input.txt","r")


"""
https://woohyun-king.tistory.com/428 -> 이 링크 참고함..
문제
인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 승원이는 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
M = 3이고, 바이러스를 아래와 같이 놓은 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 바이러스를 놓은 위치는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.

6 6 5 4 - - 2
5 6 - 3 - 0 1
4 - - 2 - 1 2
3 - 2 1 2 2 3
2 2 1 0 1 - -
1 - 2 1 2 3 4
0 - 3 2 3 4 5
시간이 최소가 되는 방법은 아래와 같고, 5초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.

0 1 2 3 - - 2
1 2 - 3 - 0 1
2 - - 2 - 1 2
3 - 2 1 2 2 3
3 2 1 0 1 - -
4 - 2 1 2 3 4
5 - 3 2 3 4 5
연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.

입력
첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

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
5

"""
from itertools import combinations
from collections import deque

N , M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]


# 바이러스 위치 저장
virus = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            virus.append((i,j))


result = []

for virus_comb in combinations(virus, M):
    max_time= float("-inf")  # ** max값을 구하는거니까 float("-inf") ***
    flag = True
    visited = [[-1] * N for _ in range(N)]


    for vx,vy in virus_comb:
        visited[vx][vy] = 0


    queue = deque(virus_comb)

    while queue:
        x, y = queue.popleft()

        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if 0<= nx < N and 0<= ny < N and visited[nx][ny] == -1 and maps[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    
    for i in range(N):
        for j in range(N):
            if maps[i][j] != 1:  # 벽이 아니면
                max_time = max(max_time, visited[i][j]) # 각 칸에 퍼뜨려진 시간 넣기

            if maps[i][j] != 1 and visited[i][j] == -1:  # 벽이 아니고, 방문하지도 않은건,
                flag = False  # 퍼뜨릴 수 없는거


    if not flag:  # 퍼뜨릴 수가 없으면 일단, continue
        continue
    else: # result에 maxtime들을 넣어줌.
        result.append(max_time)


# result가 비어있지 않으면
if len(result) != 0:
    print(min(result))  # 최소 시간 리턴

else: # result가 비어있으면
    print(-1)  # -1리턴
 



























# # 바이러스 놓일 수 있는 위치 좌표 저장
# virus = []

# for i in range(N):
#     for j in range(N):
#         if maps[i][j] == 2:
#             virus.append((i,j))

        
# # 최소 바이러스 감염시간리스트
# result = []

# # 조합으로 바이러스 위치 M개 선택
# for viruses in combinations(virus, M):
#     visited = [[-1] * N for _ in range(N)]  # -1은 방문안된거, 0>=은 감염된 시간
#     flag = True
#     maxtime = float("-inf")  # 이걸 구해야 가장 작게 퍼지는 최소 시간을 구할 수 있음.


#     # 바이러스 위치 저장
#     for vx, vy in viruses:
#         visited[vx][vy] = 0

#     queue = deque(viruses)

#     while queue:
#         x,y = queue.popleft()

#         dx = [-1,0,1,0]
#         dy = [0,1,0,-1]

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0<= nx < N and 0<= ny < N and visited[nx][ny] == -1 and maps[nx][ny] != 1:
#                 visited[nx][ny] = visited[x][y] + 1  # 여기를 x,y로 했어야돼....
#                 queue.append((nx,ny))

    
#     for i in range(N):
#         for j in range(N):
#             if maps[i][j] != 1:  # 모든 빈칸에 바이러스가 퍼지는 최소 시간을 기록하기 위해서 이 코드가 진짜 꼭 필요해, 이걸 안하면 제대로 된 시간을 구할 수 없음.
#                 maxtime = max(maxtime, visited[i][j])

#             if maps[i][j] != 1 and visited[i][j] == -1:  # 바이러스를 아예 퍼뜨릴 수 없는 경우
#                 flag = False  # false로

#     if not flag:  # 모든 칸에 바이러스를 퍼뜨릴 수 없는 경우
#         continue

#     else:
#         result.append(maxtime)

# if not result:
#     print(-1)
# else:
#     print(min(result))










