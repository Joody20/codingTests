def solution(dirs):
    x,y,paths = 0 , 0, set()  # paths는 유일해야함.
    direct = { 'U' : [0,1] , 'D' : [0,-1] , 'R':[1,0], 'L' : [-1,0]}  # 방향 선언 해주고
    
    for i in dirs: 
        dx = x + direct[i][0]
        dy = y + direct[i][1]
        
        if((-5<=dx<=5) and (-5<=dy<=5)):
            paths.add((x,y,dx,dy)) 
            paths.add((dx,dy,x,y))
            x , y = dx, dy # x,y 좌표를 dx, dy로
            
    return len(paths) // 2
    