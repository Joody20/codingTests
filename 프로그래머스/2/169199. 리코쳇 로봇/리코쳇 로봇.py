from collections import deque
def solution(board):
    n,m = len(board), len(board[0]) # n 세로 , m 가로
    visited = [[False for _ in range(m)] for _ in range(n)]
    start = [-1,-1]
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = [i,j]  # 시작점 찾기
                break
            
            
    def move(x,y,dir):
        while True:
            x += dx[dir]
            y += dy[dir]
            
            if x < 0 or x >= n or y < 0 or y >= m: # 보드를 넘어가면
                break
            elif board[x][y] == 'D': # 장애물 있으면 break
                break
                
        x -= dx[dir]
        y -= dy[dir]
        return [x,y]
    
    
    queue = deque()
    queue.append([start[0],start[1],0])
    
    while queue:
        mx,my,dis = queue.popleft()
        
        for i in range(4):
            xx,yy = move(mx,my,i) # move함수에 dir부분에 이제 상하좌우 방향 i 넘기기
        
            # 방문한 곳이면 continue
            if visited[xx][yy]:
                continue
            # 목적지 도착 했으면 dis + 1 최소 움직임 리턴
            elif board[xx][yy] == 'G':
                return dis + 1
            
            else:
                queue.append([xx,yy,dis+1])
                visited[xx][yy] = True
                
    return -1
        
                
        
        
    