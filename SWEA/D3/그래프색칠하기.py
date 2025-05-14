import sys
sys.stdin = open("input.txt","r")
"""
N개의 노드로 구성된 그래프의 노드를 M개의 색상을 이용해 칠하려고 한다.

그래프에 대한 정보가 주어지면 모든 인접한 노드 쌍에 대해, 두 노드를 서로 다른 색으로 칠하는 것이 가능한지 알아내는 프로그램을 만드시오.

노드 번호는 1에서 N번까지이고, M은 2, 3, 4 중 하나이다. 칠할 수 있는 경우 1, 칠할 수 없는 경우 0을 출력한다.

다음은 2가지 색으로 칠할 수 있는 그래프와 칠할 수 없는 그래프의 예이다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 노드의 개수 N, 간선의 개수 E, 사용할 수 있는 색상수 M이 주어지고, E개의 줄에 걸쳐 간선의 양끝 노드 번호가 주어진다.

3<=N<=20, 2<=E<=100, 2<=M<=4
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.


예제 1
2
4 4 2
1 2
1 3
2 4
3 4
4 5 2
1 2
1 3
2 4
3 4
2 3

출력 1

#1 1
#2 0

"""
def is_safe(node, graph, color, c):  # 인접노드와 같은 색인지 확인
    for neigh in graph[node]:  # 인접 노드 가져오고
        if color[neigh] == c:  # 그 인접노드의 색이 지금 컬러와 같으면 false 리턴
            return False
    return True # 아니면 True 넘겨주고

def graph_coloring(graph, M, color, node):
    if node == len(graph):    # 이 때 이제 True 넘겨주구!!
        return True
    
    for c in range(1, M+1):  # M개의 색깔 
        if is_safe(node, graph, color, c):  # 인접한 노드와 색이 다른거 확인 됐으면
            color[node] = c # 그 노드 색 입혀주고
            if graph_coloring(graph, M, color, node + 1):  # 다음 노드 확인
                return 1 # True 맞으면 1 리턴해줘
            color[node] = 0 # 백트래킹 -> 다른 노드와도 비교해줘야 돼서 다시 0으로 돌려놓기 해줘야됌.

    return 0 # 색 안칠해지면 0리턴

T = int(input())

for i in range(T):
    N , E, M = map(int,input().split())

    graph = [[] for _ in range(N+1) ]

    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    color = [0] * (N+1)
    print(f"#{i+1} {graph_coloring(graph,M,color,0)}")