def solution(n,vertex):
    # 그래프 만들기
    graph = [[] for _ in range(n+1)]
    #vertex 생성
    for (a,b) in vertex:
        graph[a].append(b)
        graph[b].append(a)
        
    #distance 설정 꼭 잘해주기
    distances = [-1] * (n + 1)
    distances[1] =  0 # 자신의 노드에서는 아직 거리가 0 이자나
    queue = [1] # 이제 시작하면 1이 되겠지
    front = 0
    
    
    while front < len(queue):
        current_node = queue[front]
        front += 1
        current_distance = distances[current_node]
        
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1: # 아직 이웃한걸 방문한게 아니면 
                distances[neighbor] = current_distance + 1 # 이웃의 거리는 현재 노드 에서 하나 더 머니까 "+1"
                queue.append(neighbor) # queue에서 이웃된걸 넣어 이미 계산한걸 또 계산하지 않게
                
    max_distance = max(distances)
    return distances.count(max_distance)