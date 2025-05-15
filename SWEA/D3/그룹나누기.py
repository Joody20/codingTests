import sys
sys.stdin = open("input.txt")

"""
수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다. 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M, 다음 줄에 M 쌍의 번호가 주어진다. 2<=N<=100, 1<=M<=100

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

예제 1
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 

출력 1
#1 3
#2 2
#3 3

"""
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a

T = int(input())

for t in range(T):
    N , M = map(int,input().split())

    numbers = list(map(int,input().split()))  # 항상 이게 2*M길이라는거여
    parents = [i for i in range(N+1)]  # 

    # M개의 쌍을 유니온 연산
    for i in range(0, 2 * M, 2):
        a = numbers[i]
        b = numbers[i + 1]
        union(parents, a, b)

    
    # 각 노드의 최종 노드 확인
    team = set()
    for i in range(1,N+1):
        team.add(find(parents,i))

    print(f"#{t+1} {len(team)}")




