import heapq
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())


def dijkstra(start,end):
    distance = [float("inf")] * (n+1)
    parent = [-1] * (n+1)
    distance[start] = 0

    heap = []

    heapq.heappush(heap, (0,start)) # 거리,현재노드

    while heap:
        dist , cur = heapq.heappop(heap)

        if dist > distance[cur]:
            continue

        for next , cost in graph[cur]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                parent[next] = cur # 이전 노드 기록
                heapq.heappush(heap, (new_cost, next))


    # 경로 추적
    path = []
    node = end
    while node != -1:
        path.append(node)
        node = parent[node]

    path.reverse() # 시작부터 end까지 

    return distance[end] , path



min_cost , paths = dijkstra(start,end)

print(min_cost)
print(len(paths))
print(" ".join(map(str,paths)))
