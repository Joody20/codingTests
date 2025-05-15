import sys
sys.stdin = open("input.txt")
"""
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 

1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

예제 1
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

출력 1

#1 2
#2 13
#3 22

"""
# 4. parent노드 찾기
def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

# 5. 두 집합을 하나로 합침
def union_parent(parent, a,b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

T = int(input())
for t in range(T):
    V,E = map(int,input().split())

    edges = []
    for _ in range(E):
        a,b, w = map(int,input().split())
        edges.append((w,a,b))  # 가중치 , 앞노드, 뒤노드

    edges.sort()  # 1. 가중치 기준으로 오름차순 정렬

    # 2. 초기 부모 설정
    parent = [i for i in range(V+1)]

    result = 0 # 최소 비용 합

    for w,a,b in edges:
        # 3. 사이클이 발생하지 않으면 선택!
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent,a,b)
            result += w


    print(f"#{t+1} {result}")