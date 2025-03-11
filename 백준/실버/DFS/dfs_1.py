"""
N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다. 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 
서로 연결되어 있는 것으로 간주합니다. 이 때, 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.


예제
4 5
00110
00011
11111
00000

"""

import sys
sys.stdin = open("input.txt","r")



def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:  # 현재 노드를 아직 방문하지 않았다면,
        graph[x][y] = 1 # 그 노드를 방문 처리


        # 상하좌우로 해주는거임.

        dfs(x-1, y) 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

        return True
    
    return False


N, M = map(int,input().split())

graph = []  # 2차원 배열 생성
for i in range(N):
    graph.append(list(map(int,input())))

# 음료수 붓기
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True: # 방문 된거라면
            result += 1 # 카운트 1씩 늘려

print(result)

