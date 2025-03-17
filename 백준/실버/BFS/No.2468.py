"""
백준 안전영역(실버 1) : https://www.acmicpc.net/problem/2468
https://sunghyun98.tistory.com/42?category=951954 -> 이 링크 도움.

어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.


첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
 
예제 1             출력
5                 5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7


예제 2             6
7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")


def bfs(height,k,j):   
    queue = deque() # deque 선언
    queue.append((k,j))  # 좌표 넣어주고

    while queue:
        x,y = queue.popleft() # 가장 앞에 값 가져와
        for i in range(4):
            nx = x + dx[i] # 새로운 방향 넣어주고
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:  # 이 좌표값이 범위 안에 있고
                if graph[ny][nx] > height and visited[ny][nx] == 0: # 현재 높이 정보가 현재 높이보다 높고 방문 되어 있지 않다면
                    visited[ny][nx] = 1  # 방문처리해주고
                    queue.append((nx,ny)) # queue에는 새로운 좌표 다시 넣어줌.

dx = [0,0,1,-1]  # x축
dy = [1,-1,0,0] # y축


N = int(input())
graph = []
maxinum = 0
for _ in range(N):  # N크기의 2차원 배열 만들고
    nums = list(map(int,input().split()))
    graph.append(nums)
    for i in range(N):  # 2차원 배열에서 가장 큰 높이를 구해.
        maxinum = max(maxinum,nums[i])


safe_area = []
for i in range(maxinum+1):  # 비는 0부터 최대 높이까지 내릴 수 있다.
    visited = [[0] * N for _ in range(N)]  # 2차원 배열의 visited배열로 하기
    cnt = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:  # N개의 배열로 된 높이 정보들에서 현재 높이보다 크고 아직 방문하지 않았다면,
                visited[j][k] = 1 # 방문시켜주고
                bfs(i,k,j) # bfs로 보내
                cnt += 1 # cnt 하나씩 세주고

    safe_area.append(cnt) # 그 횟수 safe_area에 넣기

print(max(safe_area)) # 가장 최대값 출력





