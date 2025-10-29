# 특정 원소가 속한 집합 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# 원소가 속합 집합 합치기
def union(parent, a, b):
    a = find(parent,a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v = int(input())
e = int(input())

# 부모 배열
parent = [0] * (v+1) 

# **** 부모 배열을 자기 자신 숫자로 
for i in range(1,v+1):
    parent[i] = i


edges = []         # 간선들을 넣을 배열
result = 0         # 최소 비용

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

# 간선들을 오름차순 정렬로 해줌.
edges.sort()


# 모든 간선들을 이제 검사를 해줄거에요!
for edge in edges:
    cost,a,b = edge

    if find(parent,a) != find(parent,b):
        union(parent, a, b)
        result += cost

print(result)

