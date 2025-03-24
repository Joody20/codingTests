"""
백준 퍼즐 (골드 2): https://www.acmicpc.net/problem/1525

3×3 표에 다음과 같이 수가 채워져 있다. 오른쪽 아래 가장 끝 칸은 비어 있는 칸이다.

어떤 수와 인접해 있는 네 개의 칸 중에 하나가 비어 있으면, 수를 그 칸으로 이동시킬 수가 있다. 물론 표 바깥으로 나가는 경우는 불가능하다. 우리의 목표는 초기 상태가 주어졌을 때, 최소의 이동으로 위와 같은 정리된 상태를 만드는 것이다. 다음의 예를 보자.

가장 윗 상태에서 세 번의 이동을 통해 정리된 상태를 만들 수 있다. 이와 같이 최소 이동 횟수를 구하는 프로그램을 작성하시오.

세 줄에 걸쳐서 표에 채워져 있는 아홉 개의 수가 주어진다. 한 줄에 세 개의 수가 주어지며, 빈 칸은 0으로 나타낸다.

첫째 줄에 최소의 이동 횟수를 출력한다. 이동이 불가능한 경우 -1을 출력한다.

예제 1       출력 1
1 0 3       3
4 2 5
7 8 6

예제 2       출력 2
3 6 0       -1
8 1 2
7 4 5

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")


def bfs():
    queue = deque([graph])
    visited = dict()
    visited[graph] = 0

    while queue:
        cur = queue.popleft()
        cnt = visited[cur]

        if cur == answer:
            return cnt
        
        idx = cur.index('0')
        y = idx // 3   # 열
        x = idx % 3  # 행


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 3 or ny < 0 or ny >=3:
                continue

            nidx = ny * 3 + nx
            next = list(cur)
            next[idx] , next[nidx] = next[nidx] , next[idx]

            next = ''.join(next)

            if visited.get(next , 0) == 0:
                visited[next] = cnt + 1
                queue.append(next)
    return -1


graph = ""
answer = "123456780"

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(3):
    row = input().strip().replace(' ','')
    graph += row

print(bfs())