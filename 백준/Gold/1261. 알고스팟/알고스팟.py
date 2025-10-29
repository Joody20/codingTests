from collections import deque

M,N = map(int,input().split())      # M:가로, N이 세로
matrix = [list(map(int,input())) for _ in range(N)]


# 0,1 가중치 그래프 이걸 생각하는게 진짜 중요한거네..
dist = [[-1]*M for _ in range(N)]
dist[0][0] = 0         # 시작점은 가중치가 0이겟져?


queue = deque()
queue.append((0,0)) # 시작점

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if dist[nx][ny] == -1:  # 현재 좌표의 dist가 -1인 경우 즉, 이제 처음 방문하는 경우겟지?
            if matrix[nx][ny] == 1:  # 벽이 있는 경우
                dist[nx][ny] = dist[x][y] + 1 # 그 dist 가중치 그래프에 가중치를 1 더해야함.
                queue.append((nx,ny)) # 좌표 넘겨주고
            else: # 싹 다 빈방인 경우
                dist[nx][ny] = dist[x][y]      # 1 더하지는 않고 그냥 현재 가중치를 넘김
                queue.appendleft((nx,ny))        # 빈방인 경우가 우선이라 맨 앞에 넣어줌 좌표를!!


print(dist[N-1][M-1])
