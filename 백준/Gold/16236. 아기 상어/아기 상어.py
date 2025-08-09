from collections import deque
N = int(input())
states = [list(map(int,input().split())) for _ in range(N)]


dx = [-1,0,1,0]
dy = [0,-1,0,1]

x,y,shark_size = 0,0,2

#상어 위치
for i in range(N):
    for j in range(N):
        if states[i][j] == 9: # 9가 상어의 위치야
            x = i
            y = j


def bfs(x,y,shark_size):
    distance = [[0]* N for _ in range(N)] # 거리 체크 해줘야 되니까
    visited = [[0] * N for _ in range(N)] # 방문 체크

    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    temp = []

    while queue:
        cx , cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < N and 0<= ny < N and visited[nx][ny] == 0:
                if states[nx][ny] <= shark_size: # 아기 상어 크기가 더 크다면,
                    queue.append((nx,ny)) # 그 물고기 위치 queue에 넣어주고
                    visited[nx][ny] = 1 # 방문 처리 해주고
                    distance[nx][ny] = distance[cx][cy] + 1 # 그 물고기 위치까지 이동했으니까 거리 계산해주고,
                    if states[nx][ny] < shark_size and states[nx][ny] != 0: # 아기상어의 크기가 더 크고, 0이 아니면 지나갈 수는 있어.
                        temp.append((nx,ny,distance[nx][ny])) # temp에 지금 위치랑 거리 넣어줌.

    # 거리가 가까운 물고기가 많다면, 가장 위껄로, 그것도 많다면, 가장 왼쪽껄로 -> 이렇게 구현!
    return sorted(temp, key= lambda x : (-x[2], -x[0], -x[1]))

cnt = 0
res = 0
while True:
    shark = bfs(x,y,shark_size) # 현재 상어 위치와 크기로 갈 수 있고 먹을 수 있는 물고기 후보들을 거리순, 위치순 정렬해서 리스트로 받아.

    if len(shark) == 0:  # bfs 결과가 걍 0이야 그럼 걍 종료.
        break

    nx,ny,dist = shark.pop() # 가장 가까운(거리가 제일 작은), 가장 위(행이 작은), 가장 왼쪽(열이 작은) 물고기 위치와 거리 꺼냄


    # 시간 더해주기
    res += dist # 아기 상어가 이동한 거리를 res에 더해줌!
    states[x][y] , states[nx][ny] = 0,0 # 상어가 있던 자리랑 물고기가 있던 자리를 0으로 만들어줌!!!!!!! 물고기를 먹으면, 그 칸은 빈 칸이 된다.!!

    # 상어 좌표를 먹은 물고기 좌표로 옮겨준다
    x,y= nx, ny
    cnt += 1 # 먹은 물고기 수 1 증가
    if cnt == shark_size:  # 물고기 수와 shark의 크기가 같으면
        shark_size += 1  # 상어의 크기 1 증가
        cnt = 0 # 먹은 물고기 수 초기화

print(res)
        