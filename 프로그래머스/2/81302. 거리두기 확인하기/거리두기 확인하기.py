from collections import deque

def bfs(place):
    start = []  # 시작지점을 다 넣었음.
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                seat = ([i,j])
                start.append(seat)
    
    for s in start:
        queue = deque([s])  # 큐에 시작점!즉 초깃값!
        visited = [[0]*5 for _ in range(5)]  # 방문 체크 배열
        distance = [[0]*5 for _ in range(5)] # 경로 길이 체크 배열
        visited[s[0]][s[1]] = 1  # 첫 시작 점 방문 체크 !
        
        
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<= nx < 5 and 0<= ny < 5 and visited[nx][ny] == 0:
                    if place[nx][ny] == 'O':
                        queue.append([nx,ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                    if place[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0                  
                    
    return 1


def solution(places):
    res = []
    
    for place in places:
        res.append(bfs(place))
        
    return res