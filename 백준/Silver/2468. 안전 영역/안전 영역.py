from collections import deque
def bfs(height,j,k):
    queue = deque()
    queue.append((k,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N:
                if graph[ny][nx] > height and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((nx,ny))


dx = [0,0,1,-1]
dy = [1,-1,0,0]


N = int(input())
graph = []
maximum = 0


for _ in range(N):
    nums = list(map(int,input().split()))
    graph.append(nums)
    for i in range(N):
        maximum = max(maximum,nums[i])  # 최대 높이 구하기


safe_area = []
for i in range(maximum+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                visited[j][k] = 1
                bfs(i,j,k)
                cnt += 1

    safe_area.append(cnt)


print(max(safe_area))




