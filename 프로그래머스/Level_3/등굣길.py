def solution(m, n, puddles):
    grid = [[0] *(m+1) for _ in range(n+1)]
    grid[1][1] = 1
    
    puddles_set = {(y,x) for x,y in puddles}
    
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if ((i,j) == (1,1) or (i,j) in puddles_set):
                continue
                
            if i > 1:
                grid[i][j] += grid[i-1][j]
                
            if j > 1:
                grid[i][j] += grid[i][j-1]
                
            grid[i][j] %= 1000000007
            
    return grid[i][j]