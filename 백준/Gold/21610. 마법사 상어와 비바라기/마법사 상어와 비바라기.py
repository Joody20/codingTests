N, M =map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
info = [list(map(int,input().split())) for _ in range(M)]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]


clouds = [(N-1,0), (N-1,1) , (N-2,0), (N-2,1)] # 비구름 생김.

for dir, step in info:
    # 1. 구름 이동
    new_clouds = []
    visited = [[False]* N for _ in range(N)]
    for x,y in clouds:
        nx = (x + dx[dir-1] * step) % N
        ny = (y+ dy[dir-1] * step) % N

        new_clouds.append((nx,ny))
        A[nx][ny] += 1 # 2. 비내려서 물의 양이 1 증가함
        visited[nx][ny] = True

    clouds = new_clouds # 3. 구름 사라지고 새로운 구름


    # 3. 물복사 버그
    diag_dx = [-1,-1,1,1]
    diag_dy = [-1,1,1,-1]

    for x,y in clouds:
        cnt = 0 

        for i in range(4):
            nx = x + diag_dx[i]
            ny = y + diag_dy[i]

            if 0<= nx < N and 0<= ny < N and A[nx][ny] > 0:
                cnt += 1 # 물이 있는 바구니 수 만큼

        A[x][y] += cnt # nx,ny에 있는 바구니의 물의 양이 증가


    # 4. 새구름 생성
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and A[i][j] >= 2:
                A[i][j] -= 2
                new_clouds.append((i,j))


    clouds = new_clouds

total = 0
for a in A:
    for all in a:
        total += all

print(total)