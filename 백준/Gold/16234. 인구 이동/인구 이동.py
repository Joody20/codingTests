from collections import deque

N, L, R = map(int,input().split())
grounds = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * (N) for _ in range(N)]


dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y,L,R):
    queue = deque()
    queue.append([x,y])

    visited[x][y] = True
    union = [[x,y]] # 연합에 속한 나라 좌표

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N and not visited[nx][ny]:
                diff = abs(grounds[x][y] - grounds[nx][ny])

                if L <= diff <= R:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    union.append([nx,ny])  # 연합에 추가


    if len(union) > 1:
        # 연합을 이루고 있는 각 칸의 인구수 계산을 해줌. (연합의 인구수) / 연합을 이루고 있는 칸의 개수
        union_sum = sum(grounds[cx][cy] for cx,cy in union) // len(union)

        for cx,cy in union:
            grounds[cx][cy] = union_sum

        return union
    
    else:
        return []
    


team = 0 # 팀의 개수
day = 0 # 날짜 세기
tmp_sum = 0 # 인구수


while True:
    visited = [[False] * N for _ in range(N)]
    moved = False  # 인구 이동 확인


    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 이 좌표를 방문하지 않았으면,
                union = bfs(i,j,L,R)  # bfs함수에 보내고
                if union:  # 연합된 팀이 있으면 인구 이동
                    moved = True # 인구이동 true

    if not moved:  # 인구 이동이 없으면
        break   # 걍 break
    

    day += 1  # 이동될때 이제 day 세어주는거야.

print(day)
