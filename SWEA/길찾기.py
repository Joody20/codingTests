"""
그림과 같이 도식화한 지도에서 A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.
길 중간 중간에는 최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.
다음과 같이 길이 주어질 때, A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라.
 - A와 B는 숫자 0과 99으로 고정된다.
 - 모든 길은 순서쌍으로 나타내어진다. 위 예시에서 2번에서 출발 할 수 있는 길의 표현은 (2, 5), (2, 9)로 나타낼 수 있다.
 - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.
 - 단 화살표 방향을 거슬러 돌아갈 수는 없다.

[제약사항]
출발점은 0, 도착점은 99으로 표현된다.
정점(분기점)의 개수는 98개(출발점과 도착점 제외)를 넘어가지 않으며, 한 개의 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다.
아래 제시된 가이드 라인은 제안사항일 뿐 강제사항은 아니다.

[데이터 저장 가이드]
정점(분기점)의 개수가 최대 100개 이기 때문에, size [100]의 정적 배열 2개을 선언하여, 각 정점의 번호를 주소로 사용하고, 저장되는 데이터는 각 정점에서 도착하는 정점의 번호를 저장한다.
위 그림을 저장하였을 때 결과는 다음과 같다.



[입력]
총 10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호와 길의 총 개수가 공백으로 분리되어 주어진다.
그 다음 줄에는 순서쌍이 주어진다. 순서쌍의 경우, 별도로 나누어 표현되는 것이 아니라 숫자의 나열이며, 나열된 순서대로 순서쌍을 이룬다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답(가능 여부)을 출력한다.
가능할 경우 1, 불가능할 경우 0을 출력한다.

"""



import sys
sys.stdin = open("input.txt","r")


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if visited[v] == False:
            visited[v] = True
        dfs(i)

for k in range(10):
    T , N = map(int,input().split())
    li = list(map(int,input().split()))

    graph = [[] for _ in range(100)]
    visited = [False] * 100

    for i in range(N):
        x,y = li[2*i] , li[2*i+1]
        graph[x].append(y)

    dfs(0)

    if visited[99] == True:  # 마지막 지점 B가 true이면 1을 리턴하고
        print(f"{k+1} 1")
    else:     # False면은 0을 리턴해줌.
        print(f"{k+1} 0")

