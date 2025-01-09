T = int(input())
dx=[0 ,1 ,0, -1]  # 왼쪽 / 오른쪽
dy=[1 ,0 ,-1 ,0]  # 위 /  아래


for test_case in range(1, T + 1):
    N = int(input())  # N의 크기를 가져오고
    maze =[[0]* N for _ in range(N)]  # N의 크기 만큼 배열을 만드는거 같은데 만약 N이 3이면 3x3의 maze를 짜는거지.

    x,y = 0,0
    count = 1 # 미로에 채울 숫자
    d = 0 # 방향 인덱스래 (0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위)

    for _ in range(N*N):
        maze[x][y] = count #maze에 x,y 좌표에 들어갈 숫자 count

        nx,ny = x + dx[d] , y + dy[d] # 다음 위치 계산?

        if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 0: # 다음 위치가 범위 내에 있고, 아직 방문하지 않은 거라면
            maze[nx][ny] == 0
            x,y = nx, ny # x,y를 nx,ny로 이동
        else: # 범위를 벗어나거나 이미 방문한 경우
            d = (d+1) % 4 # 오른쪽으로 튼다고? 아 그럼 이제 다시 0 뭐 이런식으로 되려나?
            x,y = x + dx[d] , y + dy[d] # 새로운 방향으로 이동
        count += 1 # 다음숫자?

    print(f"#{test_case}")
    for row in maze:
        print(" ".join(map(str,row))) # 행 단위로 출력, 숫자 사이에 공백 추가