def solution(n):
    dx = [1,0,-1]
    dy = [0,1,-1]
    
    triangle = [[0] * (i+1) for i in range(n)]
    
    x,y = 0,0 # 시작 위치
    count = 1
    d = 0
    
    result = []
    
        
    for _ in range(n * (n+1) // 2):
        triangle[x][y] = count
        count += 1

        nx , ny = x + dx[d] , y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny > nx or triangle[nx][ny] != 0:
            d = (d+1) % 3
            nx, ny = x + dx[d] , y + dy[d]
        x,y = nx, ny
        
    end = sum(triangle,[])
    return end