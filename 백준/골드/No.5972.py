"""
백준 골드 5(그래프[최단거리]) : 택배 배송

농부 현서는 농부 찬홍이에게 택배를 배달해줘야 합니다. 그리고 지금, 갈 준비를 하고 있습니다. 평화롭게 가려면 가는 길에 만나는 모든 소들에게 맛있는 여물을 줘야 합니다. 물론 현서는 구두쇠라서 최소한의 소들을 만나면서 지나가고 싶습니다.

농부 현서에게는 지도가 있습니다. N (1 <= N <= 50,000) 개의 헛간과, 소들의 길인 M (1 <= M <= 50,000) 개의 양방향 길이 그려져 있고, 각각의 길은 C_i (0 <= C_i <= 1,000) 마리의 소가 있습니다. 소들의 길은 두 개의 떨어진 헛간인 A_i 와 B_i (1 <= A_i <= N; 1 <= B_i <= N; A_i != B_i)를 잇습니다. 두 개의 헛간은 하나 이상의 길로 연결되어 있을 수도 있습니다. 농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N에 있습니다.

농부 현서가 선택할 수 있는 최선의 통로는 1 -> 2 -> 4 -> 5 -> 6 입니다. 왜냐하면 여물의 총합이 1 + 0 + 3 + 1 = 5 이기 때문입니다.

농부 현서의 지도가 주어지고, 지나가는 길에 소를 만나면 줘야할 여물의 비용이 주어질 때 최소 여물은 얼마일까요? 농부 현서는 가는 길의 길이는 고려하지 않습니다.


첫째 줄에 N과 M이 공백을 사이에 두고 주어집니다.

둘째 줄부터 M+1번째 줄까지 세 개의 정수 A_i, B_i, C_i가 주어집니다.

첫째 줄에 농부 현서가 가져가야 될 최소 여물을 출력합니다.

예제 1
6 8
4 5 3
2 4 0
4 1 4
2 1 1
5 6 1
3 6 2
3 2 6
3 4 4

출력 1
5

"""
import heapq
import sys
sys.stdin = open("input.txt","r")

# 기본 input 정보 받아오기
N , M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(M)]

# 그래프 만들기
graph = [[] for _ in range(N+1)]

# vertex 생성 -> 단방향이면 graph[a] 에 다른 vertex b와 가중치를 같이 넣어주면 됌. 양방향이면 b에도 (a,c) 넣어주기
for a,b,c in arr:
    graph[a].append((b,c))
    graph[b].append((a,c))


# 다익스트라 알고리즘 구현
def dijkstra(s):
    heap = []
    distance = [float("inf")] * (N+1)
    distance[s] = 0  # 자기 자신과의 거리는 0으로 해줌.

    heapq.heappush(heap,(0,s))   # heapq에 가중치과 노드를 넣어줌.

    while heap:
        dist , now = heapq.heappop(heap)  # heapq에서 heap를 pop함.

        if distance[now] < dist:  # 현재 계산된 최솟값보다 dist가 크면 볼 것도 없음. 걍 다음으로 넘어감. 즉, 지금까지 계산된 거리보다 지금 가충치가 더 크면 다음으로 넘어가.
            continue

        for next, cost in graph[now]:   # 이웃 돼 있는 노드를 확인합니다.
            new_cost = dist + cost # dist 현재 출발 지점에서 현재 노드까지의 거리 + 현재 노드에서 다음 노드까지의 거리

            if new_cost < distance[next]:  # 현재까지 계산된 것보다 cost가 더 작으면
                distance[next] = new_cost  # 그 cost로 업데이트 해주고
                heapq.heappush(heap, (new_cost,next))   # heap에도 다시 새로운 cost로 업데이트 해줘야함.

    return distance[N]

print(dijkstra(1))


