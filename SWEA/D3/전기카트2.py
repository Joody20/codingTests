import sys
sys.stdin = open("input.txt","r")
"""
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

이 경우 최소 소비량은 89가 된다.

N이 최대 16이기 때문에, N=10이 최대일 때의 계산 방법은 시간이 오래 걸릴 수 있음에 유의하라.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. ( 1<=T<=50 )

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다.  ( 3<=N<=16 )
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

"""
# 방법 1
T = int(input())

for t in range(T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    min_cost = float("inf")

    def dfs(current, visited, cost):
        global min_cost

        if cost >= min_cost:
            return 
        
        if visited == (1 << N) - 1:
            if graph[current][0] > 0:
                min_cost = min(min_cost , cost + graph[current][0])
            return
        
        for next in range(N):
            if not (visited & (1 << next)) and graph[current][next] > 0 :
                dfs(next, visited | (1 << next), cost + graph[current][next])

    dfs(0 , 1 << 0 , 0)
    print(f"#{t+1} {min_cost}")



# 방법 2
# from itertools import permutations
# T = int(input())

# for t in range(T):
#     N = int(input())
#     graph = [list(map(int,input().split())) for _ in range(N)]

#     zones = [ i for i in range(1, N)]  # 관리구역 번호
#     min_cost = float("inf") # 최소 비용

#     for path in permutations(zones):  # 사무실로 돌아오는데까지의 모든 경로
#         cost = 0 # 현재 비용
#         current = 0 # 인덱스번호 -> 사무실부터 시작

#         for next in path:
#             cost += graph[current][next]
#             current = next  # 인덱스번호를 다음으로 바꿔주는거임.

#         cost += graph[current][0] # 마지막에 이제 사무실까지 
#         min_cost = min(min_cost, cost) # 최소 비용 

#     print(f"#{t+1} {min_cost}")
        


   
            