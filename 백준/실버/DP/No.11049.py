import sys
sys.stdin = open("input.txt","r")

"""
문제
크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

입력
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.

둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)

항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 정답은 231-1 보다 작거나 같은 자연수이다. 또한, 최악의 순서로 연산해도 연산 횟수가 231-1보다 작거나 같다.

예제 1
3
5 3
3 2
2 6

출력 1
90

"""
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]    # i번째부터 j번째 행렬까지 곱하는 데 필요한 최소 연산 수

for term in range(1,N):   # (곱하려는 행렬수 - 1)  term이 1이면 두행렬을 곱하는 거, term이 2이면 세행렬을 곱하는거
    for i in range(N):
        if i + term == N:  # 범위를 벗어나면 무시 
            break

        j = i + term  # 끝 행렬 인덱스

        dp[i][j] = int(1e9)  # 시작행렬부터 끝행렬까지 최소값을 구해감.

        for t in range(i, j):  # 시작 행렬부터 끝행렬
            dp[i][j] = min(dp[i][j], dp[i][t] + dp[t+1][j] + arr[i][0]* arr[t][1] * arr[j][1])  # arr[i][0] * arr[t][1] * arr[j][1] -> 앞의 행수 * 앞의 열수 * 뒤의 열수

print(dp[0][N-1])


# def matrix(p):
#     global N

#     N = len(p) - 1 #행렬의 개수
#     dp = [[0] * N for _ in range(N)]  # dp

#     for length in range(2,N+1):  # 2부터 시작..?
#         for i in range(N - length + 1):
#             j = i + length - 1
#             dp[i][j] = float("inf")
#             for k in range(i,j):
#                 cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
#                 dp[i][j] = min(cost, dp[i][j])

#     return dp[0][N-1]  # 시작행렬 , 끝 행렬
# print(matrix(dims))

# dims = [arr[0][0]]  # 행렬의 숫자를 한줄로 숫자를 나타내줌.
# for i in arr:
#     dims.append(i[1])