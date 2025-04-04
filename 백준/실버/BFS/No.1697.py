"""
백준 숨바꼭질(실버 1) : https://www.acmicpc.net/problem/1697

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")

N , K = map(int,input().split())
visited = [0] * 100001

# N이 K가 되기 위한 최선의 방법? 이라고 해야할 까? 

# 5니끼 5를 곱하거나 1더하거나 1빼서 K를 만들어줘야돼. 

# 일단 그러면 N이 K보다 작으면 두배를 해
# 그 두배한 값이 그래도 K보다 작으면 두배를 해 그리고 K보다 크면 1을 더하거나 1을 빼
# 근데 이 횟수보다 두배 하지 않고 1을 빼거나 더하

def bfs(n):
    queue = deque([n])
    visited[n] = 0

    while queue:
        cur = queue.popleft()

        if cur == K :
            return visited[K]
        
        for i in (cur+1, cur-1, cur * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[cur] + 1
                queue.append(i)

print(bfs(N))