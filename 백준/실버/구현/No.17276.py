"""
백준 실버 1: 배열 돌리기 https://www.acmicpc.net/problem/17276 

크기가 n x n인 2차원 정수 배열 X가 있다. (n은 홀수)

X를 45° 의 배수만큼 시계방향 혹은 반시계방향으로 돌리려고 한다. X를 시계 방향으로 45° 돌리면 아래와 같은 연산이 동시에 X에 적용되어야 한다:

X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다. 
X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
X의 가운데 행을 X의 주 대각선으로 옮긴다.
위 네 가지 경우 모두 원소의 기존 순서는 유지 되어야 한다.
X의 다른 원소의 위치는 변하지 않는다.
반시계 방향으로 45° 돌리는 경우도 위와 비슷하게 정의된다.

예를 들어, 아래 그림 중앙에 5x5 배열 X가 있고, 이 배열을 시계방향 혹은 반시계방향으로 45° 돌렸을 때의 결과가 우측 그리고 좌측에 있다. 굵은 원소는 주 대각선 / 중간 열 / 부 대각선 / 중간 행에 위치한 원소이다.


첫 줄에 테스트 케이스의 수 T가 주어진다 (1 ≤ T ≤ 10).

각 테스트 케이스에 대해: 첫 줄에 배열의 크기를 나타내는 n (1 ≤ n < 500, n은 홀수) 그리고 각도 d가 주어진다. d는 0 ≤ |d| ≤ 360 을 만족하며 |d| 는 45의 배수이다. d가 양수이면 시계방향으로 d° 돌려야 하고, 음수이면 반시계방향으로 |d|° 돌려야 한다. 다음 n줄에 걸쳐 각 줄에 n개의 정수가 공백으로 구분되어 주어진다 (X의 원소들을 나타낸다). 각 값은 1 이상 1,000,000 이하의 정수이다.

각 테스트 케이스에 대해 회전 연산을 마친 후 배열의 상태를 출력한다. n줄에 걸쳐 각 줄에 n개의 정수를 공백으로 구분하여 출력한다. 


"""
from copy import deepcopy
import sys
sys.stdin = open("input.txt","r")

T = int(input())

for _ in range(T):
    N , d = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    ans = [[0] * N for _ in range(N)]

    if d < 0:  # 반시계 방향
        d += 360

    if d == 360 or d == 0:
        for i in board:
            print(*i)

    else:
        for _ in range(d//45):
            mid = N // 2  # 가운데 행을 미리

            for i in range(N):
                for j in range(N):
                    if j == mid:  # 주대각선 -> 가운데열
                        ans[i][j] = board[i][i]
                    elif i + j == N - 1: # 가운데열 -> 부대각선
                        ans[i][j] = board[i][mid]
                    elif i == mid: # 부대각선 -> 가운데행
                        ans[i][j] = board[N-j-1][j]
                    elif i == j: # 가운데행 -> 주대각선
                        ans[i][j] = board[mid][j]
                    else:   # 원래 보드에 있는 값은 그대로
                        ans[i][j] = board[i][j]

            board = deepcopy(ans)


        for k in ans:
            print(*k)



