import sys
sys.stdin = open("input.txt","r")

"""
출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

(표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)

인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.

색이 칠해진 칸을 따라 이동하는 경우 기본적인 연료 소비량 4에, 높이가 0에서 1로 경우만큼 추가 연료가 소비되므로 최소 연료 소비량 5로 목적지에 도착할 수 있다.

이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램을 만드시오.

[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N, 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.

1<=T<=50, 3<=N<=100, 0<=H<1000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

예제 1
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1

출력 1
#1 5
#2 8
#3 9

"""
import heapq

def bfs(N, grid):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    dist= [[float("inf")]* N for _ in range(N)]
    dist[0][0] = 0

    heap = [(0,0,0)]  # 연료,x,y


    while heap:
        fuel,x,y = heapq.heappop(heap)

        if x == N-1 and y == N-1:  # 이게 종점이라서 이 때 연료를 리턴해주는거임.
            return fuel
        
        for i in range(4):  # 상하좌우 방향 해주고,
            nx = x + dx[i] 
            ny = y + dy[i]

            if (0 <= nx < N and 0 <= ny < N ):
                height_diff = grid[nx][ny] - grid[x][y]   # 높이 계산해주는거임. 0 -> 1이면 더해주고 
                cost = 1 + max(0,height_diff)

                new_fuel = fuel + cost  # 새로운 연료 계산해주고
                if new_fuel < dist[nx][ny]:  # 근데 이게 더 크면
                    dist[nx][ny] = new_fuel  # 더 작은 값 dist[nx][ny] 에 넣어줌.
                    heapq.heappush(heap,(new_fuel,nx,ny))  # 새로운 비용, nx,ny 넣어주고여!

    return dist[N-1][N-1]  # 결국 마지막은 dist[N-1][N-1] 리턴

T= int(input())
for t in range(T):
    N = int(input())

    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    print(f"#{t+1} {bfs(N, graph)}")


        

