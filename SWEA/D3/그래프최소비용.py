import sys
sys.stdin = open("input.txt","r")

"""
N개의 노드로 구성된 유향 그래프에 대해 인접 노드로 이동하는 비용을 기록한 인접 행렬이 주어진다.

모든 노드 i에 대해 다른 노드 j로 이동하는 경로가 있는 경우 최소 이동 비용을 구했을 때, 이 중 가장 큰 값을 출력하는 프로그램을 만드시오.

i에서 j로 이동할 때 다른 모든 노드를 지나야 하는 것은 아니며, 인접한 노드 사이 비용이 음수인 경우는 있으나 출발한 노드로 돌아왔을 때의 비용이 음수인 사이클은 존재하지 않는다.

다음과 같은 그래프가 있을 때 인접 행렬과 이동 비용은 다음과 같다.

[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 노드의 개수 N, 다음 줄부터 출발 노드 i에 대해 다른 노드 j까지의 비용인 N개의 aij가 N 줄에 걸쳐 주어진다.

1<=T<=50, 3<=N <=100, -99<=aij<=99 (단 i != j 면서 aij==0인 경우는 인접하지 않음을 나타낸다.)

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

예제 1

3
3
0 27 44
-5 0 62
0 99 0
5
0 0 1 0 0
88 0 39 0 75
71 56 0 43 0
23 0 -21 0 92
22 -1 48 0 0
10
0 94 98 0 23 0 31 0 85 0
10 0 78 19 83 0 91 0 82 -7
70 0 0 24 0 66 0 0 46 0
0 40 90 0 82 77 0 0 0 0
72 0 61 16 0 99 0 58 -9 44
82 84 61 76 29 0 30 28 20 72
39 78 76 0 0 11 0 54 58 39
0 0 25 40 10 0 57 0 19 38
68 5 81 78 87 54 60 -7 0 0
67 56 83 74 0 36 0 55 0 0


출력 1

#1 99
#2 132
#3 92

"""
T = int(input())

for t in range(T):
    N = int(input())
    raw_graph = [list(map(int,input().split())) for _ in range(N)]

    # 초기화  -> 이걸 꼭 꼭 해줘야돼. -> 0의 값이 비용이 없는건지, 경로가 아닌건지를 확실히 해주기 위해서!
    INF = float("inf")
    graph = [[INF] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] = 0  #대각선의 값은 0
            elif raw_graph[i][j] != 0:  # 0이 아니면
                graph[i][j] = raw_graph[i][j]  # 여기에 넣어줌.


    #플로이드-워셜 알고리즘 -> i에서 j로 가는 모든 경로의 최단경로의 cost를 저장해서 최댓값을 출력하고자 할 때!
    # Floyd-Warshall 알고리즘은 그래프에서 모든 정점 쌍 간의 최단 경로를 구할 때 사용하는 알고리즘입니다.
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]  # 더 작은 값으로 맵핑
                    # graph[i][j] = min(graph[i][j] , graph[i][k]+ graph[k][j])  -> 이렇게도 가능
 

    # 최단거리 중 최댓값 구하기
    max_cost = 0
    for i in range(N):
        for j in range(N):
            if i != j  and graph[i][j] != INF:
                max_cost = max(max_cost, graph[i][j])

    print(f"#{t+1} {max_cost}")
