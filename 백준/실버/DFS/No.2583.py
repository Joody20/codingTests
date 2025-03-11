"""
백준 영역 구하기 (실버 1) : https://www.acmicpc.net/problem/2583

눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

예제
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

"""

import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가 이거 안해줬더니 백준에서 recursive error남.
sys.stdin = open("input.txt", "r")

N , M, K = map(int,input().split())

graph = [[0] * M for _ in range(N)]


# 내가 해맸던건 일단 좌표대로 직사각형 만드는게 골치 아팠음......
for _ in range(K):
    lx,ly,rx,ry = map(int,input().split())  # 이런식으로 좌표 설정 해줄 수 있었고
    for i in range(ly,ry):  # y좌표부터
        for j in range(lx,rx): # x좌표로
            graph[i][j] = 1 # 이 좌표에 들어간건 1로 해주고

dx=[0,1,0,-1]
dy = [1,0,-1,0]

square_list= []

def dfs(x,y):
    graph[x][y] = 1
    val = 1
    for i in range(4):  # 4개의 방향이 존재
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: # 이 상하좌우를 넘어가는건 무시
            continue
        if graph[nx][ny] == 0: # 0이면 
            val += dfs(nx,ny) # val 값을 하나씩 추가해
    return val

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: # 0인 위치의 좌표를 
            square_list.append(dfs(i,j)) # dfs 함수에 넘겨줌


res = len(square_list)
print(res if res > 0 else 1)
print(" ".join(map(str,sorted(square_list))))


