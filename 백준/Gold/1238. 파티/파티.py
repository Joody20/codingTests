import heapq
N, M , X = map(int,input().split())

#단방향 그래프 구현
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    reverse_graph[b].append((a,c))


def dijkstra(start,graph):
    distance = [float("inf")] * (N+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap,(0,start))

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


dist_go = dijkstra(X,graph)
dist_reverse = dijkstra(X, reverse_graph)

distances = []
for a,b in zip(dist_go, dist_reverse):
    if a+b != float("inf"):
        distances.append(a+b)

print(max(distances))