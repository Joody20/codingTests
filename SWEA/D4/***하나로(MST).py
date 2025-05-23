import sys
sys.stdin = open("input.txt","r")

"""
위와 같은 방법을 통해 인도네시아 내의 모든 섬들을 연결해야 하는 프로젝트입니다.

그림 3에서 B와 A처럼 직접적으로 연결된 경우도 있지만, B와 C처럼 여러 섬에 걸쳐 간접적으로 연결된 경우도 있습니다.

다만 인도네시아에서는 해저터널 건설로 인해 파괴되는 자연을 위해 다음과 같은 환경 부담금 정책이 있습니다.

- 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)만큼 지불

총 환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계하시오.

64비트 integer 및 double로 처리하지 않을 경우, overflow가 발생할 수 있습니다 (C/C++ 에서 64비트 integer는 long long 으로 선언).

위의 그림 2은 환경 부담금을 최소로 하며 모든 섬을 연결하고 있지만, 그림 3는 그렇지 않음을 알 수 있습니다.

[입력]

가장 첫 줄은 전체 테스트 케이스의 수이다.

각 테스트 케이스의 첫 줄에는 섬의 개수 N이 주어지고 (1≤N≤1,000),

두 번째 줄에는 각 섬들의 정수인 X좌표, 세 번째 줄에는 각 섬들의 정수인 Y좌표가 주어진다 (0≤X≤1,000,000, 0≤Y≤1,000,000).

마지막으로, 해저터널 건설의 환경 부담 세율 실수 E가 주어진다 (0≤E≤1).

20
2
0 0
0 100
1.0
4
0 0 400 400
0 100 0 100
1.0
6
0 0 400 400 1000 2000
0 100 0 100 600 2000
0.3

[출력]

각 테스트 케이스의 답을 순서대로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다. 이때 C는 케이스의 번호이다.

같은 줄에 빈칸을 하나 두고, 주어진 입력에서 모든 섬들을 잇는 최소 환경 부담금을 소수 첫째 자리에서 반올림하여 정수 형태로 출력하라.

#1 10000
#2 180000
#3 1125000
#4 1953913
#5 27365366
#6 337122
#7 711268755613
#8 280157
#9 521568761
#10 34
#11 375890356686
#12 68427157
#13 21404
#14 16620885
#15 4776395492
#16 54860981981
#17 24236206202
#18 132410
#19 12876964085
#20 7016649393
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]


def union_parent(parent, a, b):
    root_a =  find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

T = int(input())

for t in range(T):
    N = int(input()) # 섬의 개수
    X_list = list(map(int,input().split()))
    Y_list = list(map(int,input().split()))
    E = float(input()) # 환경부담세율

    edges = []
    for i in range(N):
        for j in range(i+1, N):
            dist_squared = (X_list[i] - X_list[j]) ** 2 + (Y_list[i] - Y_list[j])**2
            cost = dist_squared * E  # 가중치를 애초에 계산을 해주고 나서 해줬어야 했어
            edges.append((cost, i,j))

    # 1. 다영아 MST에서는 edges를 sort해줘야지;;;;
    edges.sort()

    # 2. parent 배열 만들어주구
    parent = [i for i in range(N+1)]

    # 3. 가중치 값 최소 비용으로 계산
    result = 0 # 초ㅣ소비용
    for w , a,b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a ,b)
            result += w

    print(f"#{t+1} {int(round(result,0))}")

    
        