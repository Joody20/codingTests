import sys
sys.stdin = open("input.txt","r")

N = int(input())


visited = [[False]*N for _ in range(N)]
graph = [] 
teacher = []  # 선생님의 좌표를 따로 저장해서, 이걸로 판단하는 생각이 잘 안들었음..
flag = False

for i in range(N):
    graph.append(list(map(str,input().split())))
    for j in range(N):
        if graph[i][j] == 'T':  # 선생님의 좌표를 저장해줄게요!
            teacher.append([i,j])

 # 백트래킹 알고리즘 구현
def back(cnt): 
    global flag
    if cnt == 3:  # 장애물을 3개 했다면,
        if dfs():
            flag = True
            return
        
    else:
        for x in range(N):
            for y in range(N):
                if graph[x][y] == 'X':  # 빈칸이면
                    graph[x][y] = 'O'  # O로 바꿔줘. 장애물 설치
                    back(cnt+1)     # 그리고 cnt + 1
                    graph[x][y] = 'X'  # 다시 이제 방문해제


# DFS 알고리즘 구현 
def dfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for t in teacher:
        for k in range(4):
            nx,ny = t  # 선생님의 좌표를 꺼내줌요.

            while 0<=nx < N and 0<=ny<N:
                if graph[nx][ny] == 'O':  # 장애물이 보이면 break
                    break

                if  graph[nx][ny] == 'S':  # 학생이 보이면?
                    return False  # 실패
                
                nx += dx[k]
                ny += dy[k]
    # 모두 통과하면 학생이 안보이는 거니까 성공임.         
    return True
            

back(0)  # 백트래킹 알고리즘 start!

if flag:  # flag이면 YES!!
    print('YES')
else:  # 아니면 NO
    print("NO")





