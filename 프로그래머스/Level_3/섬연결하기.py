def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    
    data = list(range(n))
    
    def find(x):
        if data[x] != x:
            data[x] = find(data[x])
        return data[x]
    
    def union(x,y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            data[rootY] = rootX
    
    total_cost = 0 
    edge = 0
    
    for node1, node2, cost in costs:
        if find(node1) != find(node2):
            union(node1, node2)
            total_cost += cost
            edge += 1
            
    return total_cost
            