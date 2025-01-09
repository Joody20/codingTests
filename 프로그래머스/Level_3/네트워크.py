def solution(n, computers):
    #깊이 우선 탐색을 위한 재귀 함수 정의
    def dfs(node,visited):
        visited[node] = True # 현재 노드를 방문 했음을 표시

        for neighbor in range(n):# 모든 컴퓨터를 탐색하여 현재 노드와 연결된 컴퓨터를 찾음
            if computers[node][neighbor] == 1 and not visited[neighbor]: #현재 노드와 아웃노드가 연결되어 있고 아웃노드가 아직 방문되지 않았다면
                dfs(neighbor, visited) # 아웃노드를 dfs로 탐색
                
            
    visited = [False] * n #각 컴퓨터의 방문 여부를 저장하는 배열. 초기에는 모든 False로 성정
    network_count = 0 # 네트워크의 수를 저장하는 변수
    
    for i in range(n): # 모든 컴퓨터를 탐색
        # 현재 컴퓨터가 방문되지 않았다면, 새로운 네트워크를 찾은 것임
        if not visited[i]:
            dfs(i,visited) # 해당 컴퓨터와 연결된 모든 컴퓨터를 DFS로 탐색하고 방문표시
            network_count +=1 # 네트워크의 수를 증가
    return network_count # 모든 탐색이 끝난 후, 총 네트워크 수를 반환
                