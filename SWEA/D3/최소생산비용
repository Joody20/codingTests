import sys
sys.stdin = open("input.txt","r")

"""
A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..


이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 제품 수 N이 주어지고, 이후 제품당 한 줄 씩 N개의 줄에 걸쳐 공장별 생산비용 Vij가 주어진다. 3<=N<=15,   1<=Vij<=99
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

예제 1

3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4


출력 1

#1 63
#2 78
#3 129

""" 
def dfs(depth, total):
    if total >= min_cost[0]:  # total이 최소비용보다 크면 무시,
        return
    
    if depth == N:  # 모든 제품을 다 계산했으면,갱신
        min_cost[0] = total  # min_cost를 total값으로 변경
        return
    
    for i in range(N):
        if not visited[i]:  # i번째 방문하지 않았다면,
            #백트래킹 사용
            visited[i] = True  # 그걸 true로 해주고
            dfs(depth+1, total + graph[depth][i])  # depth+1, graph[depth][i] 넘겨주기
            visited[i] = False # 다시 false로 해줌.

    return min_cost[0]
    
T = int(input())

for t in range(T):
    N = int(input())
    visited = [False] * (N+1)
    min_cost = [float("inf")] * (N+1)

    graph = [list(map(int,input().split())) for _ in range(N)]  # 가중치가 있는 그래프임
    
    print(f"#{t+1} {dfs(0,0)}")




