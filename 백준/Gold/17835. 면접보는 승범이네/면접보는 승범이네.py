import heapq

N,M,K = map(int,input().split())

graph = [[] for _ in range(N+1)]

# 단방향 -> 역방향으로 그래프 구현
for _ in range(M):
    u,v,c = map(int,input().split())
    graph[v].append([u,c])


meetingrooms = list(map(int,input().split()))

def dijkstra():
    hq = []

    for room in meetingrooms:
        heapq.heappush(hq,[0,room]) #heap으로 넣어주기!! 다익스트라이니까! (거리, 현재노드)
        distance[room] = 0


    while hq:
        dist , cur = heapq.heappop(hq)
        
        if dist > distance[cur]:
            continue

        for next, cost in graph[cur]:
            new_cost = dist + cost

            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(hq,[new_cost, next])

    return distance



max_start, max_cost = 0,0
distance = [float("inf")] * (N+1)
dijkstra()

for i,r in enumerate(distance):
    if r > max_cost and r != float("inf"):
        max_cost = r
        max_start = i

print(max_start)
print(max_cost)
