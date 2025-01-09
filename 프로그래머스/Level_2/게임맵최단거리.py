from collections import deque
def solution(maps):
    x = 1 #1,1에서 시작한다고 했으니까 
    y = 1 
    
    add = [0] * (len(maps[0])) # 5개의 빈 배열
    
    grid = [len(maps) , len(maps[0])]  # 5*5 그리드
    
    maps.insert(0,add) # maps 맨앞에 add 추가(위쪽 경계)
    
    for m in maps: 
        m.insert(0,0) # 왼쪽,오른쪽 경계
        m.append(0)
        
    maps.append(add) # 아래쪽 겅계
    
    maps[1][1] = 0 # 시작위치는 방문처리
    
    queue = deque()
    dx = [0,1,0,-1] # 오 , 왼
    dy = [1,0,-1,0] # 위 , 아래
    
    queue.append((x,y,1)) # 시작위치와 현재 이동 횟수 queue에 넣기
    
    while (queue):
        
        x,y,cnt = queue.popleft() # x,y와 이동횟수 하나씩 가져오기
        
        if(x==grid[0] and y==grid[1]): # 5,5 목표지점에 도달했다면 
            return cnt # 이동횟수 리턴하기
        for xx,yy in zip(dx,dy): 
            nx = x + xx # 다음 x좌표
            ny = y + yy # 다음 y좌표 
            if(maps[nx][ny] == 1): # 이동할 수 있다면, 1인 곳만 움직일 수 있음
                maps[nx][ny] = 0  # 방문처리 하고 
                queue.append((nx,ny,cnt+1)) # 다음 x,y좌표와 이동횟수를 queue에 넣음
                
    return -1 # 아예 목표지점에 도달할 수 없다면 -1
    
    