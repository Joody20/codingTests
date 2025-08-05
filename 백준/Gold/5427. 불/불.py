from collections import deque

def bfs(N,M,grid):
    fire_time = [ [-1] * N for _ in range(M)]
    sangin_time = [[-1] * N for _ in range(M)]

    fire_queue = deque()
    sangin_queue = deque()

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '*':  # 불의 좌표
                fire_queue.append([i,j])
                fire_time[i][j] = 0

            if grid[i][j] == '@':  # 상근이의 위치 좌표
                sangin_queue.append([i,j])
                sangin_time[i][j] = 0

    # 1. 불 먼저 퍼뜨리기
    while fire_queue:
        x,y = fire_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < M and 0<=ny < N:
                if grid[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire_queue.append([nx,ny])


    #2. 상근이 이동!!!
    while sangin_queue:
        x,y = sangin_queue.popleft()

        if x == 0 or x == M -1 or y == 0 or y == N-1:
            return sangin_time[x][y] + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < M and 0<= ny < N:
                if grid[nx][ny] == '.' and sangin_time[nx][ny] == -1:
                    # 불보다 먼저 도착할 수 있는 경우에만 탈출 시간 늘려주기
                    if fire_time[nx][ny] == -1 or sangin_time[x][y] + 1 < fire_time[nx][ny]:  # 이 코드가 너무 킥이다.....
                        sangin_time[nx][ny] = sangin_time[x][y] + 1
                        sangin_queue.append([nx,ny])


    return 'IMPOSSIBLE'



T = int(input())
for _ in range(T):
    N , M = map(int,input().split())
    grid = [list(input()) for _ in range(M)]
    print(bfs(N,M,grid))
