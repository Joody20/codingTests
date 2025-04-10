"""
백준 촌수계산(실버 2): https://www.acmicpc.net/problem/2644


우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.


사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.


예제 1
9         ->    3
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

예제2
9        -> -1
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(input()) # 전체 사람의 수
p1 , p2 = map(int,input().split())  # 촌수를 구해야 하는 두 사람

M = int(input())  # 부모관계를 관계의 수

graph = [ [] for _ in range(N+1) ]
visited = [False] * (N+1)

res = [0] * (N+1)

def bfs(start , end): 

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()  # queue에서 뺀 첫번째 꺼

        if v == end:
            return visited[v]-1
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print(queue)
                visited[i] += visited[v]+1


# 출력해야하는건 일단 p1과 p2의 촌수야 

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = bfs(p1 , p2) # 두 사람의 촌수를 넣어주는거임.
 
if ans == None:
    print('-1')
else:
    print(ans)


