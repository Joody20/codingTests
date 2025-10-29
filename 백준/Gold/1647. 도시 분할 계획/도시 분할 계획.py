import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    # rank 기반 병합 (트리 높이 최소화)
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
rank = [0] * (v + 1)

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0
last_edge = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        result += cost
        last_edge = cost

print(result - last_edge)