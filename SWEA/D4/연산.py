import sys
sys.stdin = open("input.txt","r")

"""
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


"""
from collections import deque
def mul(S,E):  # bfs 알고리즘으로 구현한거임.
    visited= set()
    queue = deque()
    queue.append((S,0))  # 시작 숫자, 연산횟수

    while queue:
        cur , count = queue.popleft()  # 현재 숫자와 연산횟수를 꺼내줌.

        if cur in visited:
            continue

        visited.add(cur)  # 현재 숫자를 visited에 넣어줌.

        if cur == E:  # 현재숫자가 M이 된 경우에 그 연산횟수를 리턴해줌,
            return count

        for next_num in (cur + 1, cur - 1, cur * 2, cur - 10):
            if 0< next_num< 1000001 and next_num not in visited:  # 이거 범위 잘못해줘서 틀렸었어.... 1000001까지로 해줬어야 햇어..
                queue.append((next_num, count + 1))
    return -1
 
T = int(input())

for t in range(T):
    N , M = map(int,input().split())
    print(f"#{t+1} {mul(N,M)}")



