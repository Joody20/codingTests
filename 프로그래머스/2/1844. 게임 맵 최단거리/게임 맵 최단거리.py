# from collections import deque
# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
    
#     visited = [[False]*(m) for _ in range(n)]
    
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
    
#     visited[0][0] = True  # 시작점 0,0은 True로 방문처리
    
#     queue = deque()
#     queue.append((0,0))
    
#     while queue:
#         x,y = queue.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0<= nx < m and 0<= ny <n:
#                 if maps[ny][nx] == 1 and visited[ny][nx] == False:
#                     visited[ny][nx] = True
#                     queue.append((nx,ny))
#                     maps[ny][nx] = maps[y][x] + 1
                    
#     if maps[n-1][m-1] == 1:
#         return -1
    
#     return maps[n-1][m-1]
          
    
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    visited[0][0] = True
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0<= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    # maps[nx][ny] = maps[x][y] + 1  # maps로 리턴하는거니까
                    queue.append((nx,ny))
                    
    if visited[n-1][m-1]:
        return visited[n-1][m-1]
    else:
        return -1
    