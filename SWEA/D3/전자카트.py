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


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


예제 1

3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

출력 1

#1 89
#2 96
#3 139


"""
def dfs(current, visited,cost):
    global min_cost

    if cost >= min_cost:
        return
    
    if visited == (1 << N) - 1:
        if graph[current][0] > 0:
            min_cost = min(min_cost, cost + graph[current][0])
        return 
    
    for next in range(N):
        if not (visited & (1 << next)) and graph[current][next] > 0:
            dfs(next, visited | (1 << next), cost + graph[current][next])

    return min_cost

T = int(input())
for t in range(T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    min_cost = float("inf")

    print(f"#{t+1} {dfs(0, (1 << 0) , 0)}")

    