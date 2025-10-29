# from collections import deque
# def bfs(maps,x,y,n,m,visited):
#     queue = deque()
#     queue.append((x,y))
    
#     visited[x][y] = True
#     area = int(maps[x][y])
    
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
    
#     while queue:
#         x,y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
        
#             if 0<= nx< n and 0 <= ny < m:
#                 if maps[nx][ny] != 'X' and visited[nx][ny] == False:
#                     visited[nx][ny] = True
#                     area += int(maps[nx][ny])
#                     queue.append((nx,ny))
#     return area

# def solution(maps):
#     n = len(maps)  # 행수
#     m = len(maps[0]) # 열 수
#     result = []
    
#     visited = [[False] * m for _ in range(n)]
                
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] != 'X' and visited[i][j] == False:
#                 result.append(bfs(maps,i,j,n,m,visited))
    
#     if len(result) > 0:
#         return sorted(result)
#     else:
#         return [-1]

from collections import deque

def bfs(maps, i, j , n, m, visited):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    queue = deque()
    queue.append([i,j])
    visited[i][j] = True
    area = int(maps[i][j])  # 식량!!!
    
    while queue:
        x,y = queue.popleft()
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0<= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                    visited[nx][ny] = True   # 방문 처리 해주고!
                    area += int(maps[nx][ny]) # 그 숫자를 더해줌 !!
                    queue.append([nx,ny]) # queue에 새로운 좌표 넣어줌
                    
    return area
                    

def solution(maps):
    n = len(maps)    # 가로
    m = len(maps[0]) # 세로
    days = 0
    result = []
    
    visited = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and maps[i][j] != 'X':
                days = bfs(maps,i,j,n,m,visited)
                result.append(days)
                
    if len(result) > 0:
        return sorted(result)
    else:
        return [-1]