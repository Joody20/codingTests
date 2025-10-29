from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(y,x,cnt,visited,n,m,land):
    queue = deque()
    queue.append([y,x])
    visited[y][x] = cnt
    count = 1
    
    while queue:
        y,x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx < n and 0<=ny < m and visited[ny][nx] == 0 and land[ny][nx] == 1:
                visited[ny][nx] = cnt
                queue.append([ny,nx])
                count += 1
                
    return count
                  
    
def solution(land):
    N = len(land[0]) # 가로
    M = len(land)    # 세로
    
    cnt = 1
    oils = {}
    answer = []
    
    visited = [[0] * N for _ in range(M)]
    
    for i in range(N):
        for j in range(M):
            if land[j][i] == 1 and visited[j][i] == 0:
                oils[cnt] = bfs(j,i,cnt,visited,N,M,land)
                cnt += 1
                
    for x in range(N):  # 한 열을 탐색
        total_land = 0
        tmp = set()
        for y in range(M): # 그 열의 모든 행을 확인
            if visited[y][x] != 0:  # 방문하지 않았다면
                tmp.add(visited[y][x])   # 그 위치의 모든 땅들을 tmp에 넣음
                
        for i in tmp:
            total_land += oils[i] # 2,1,1,12 다 더한걸 이제 answer
        answer.append(total_land)
        
    return max(answer)
            
    
    
  
    