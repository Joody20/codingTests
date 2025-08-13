import heapq
V , E = map(int,input().split())
K = int(input())

graph =[[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


def dijkstra(start):
    heap = []
    distance = [float("inf")] * (V+1)
    distance[start] = 0

    heapq.heappush(heap,(0,start)) # 거리,현재노드

    while heap:
        dist, cur = heapq.heappop(heap)

        if dist > distance[cur]:
            continue


        for next, cost in graph[cur]:
            new_cost = cost + dist

            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(heap,(new_cost, next))

    return distance


distances = dijkstra(K)

for i in distances[1:]:
    if i == float("inf"):
        print('INF')
    else:
        print(i)
    