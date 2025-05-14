import sys
sys.stdin = open("input.txt")

"""
1부터 N까지 양의 정수를 원소로 갖는 집합이 있다. 이 집합의 모든 부분 집합에 대해 원소의 합이 K인 경우의 수 M을 알아내려고 한다.

부분 집합의 개수는 2N개이기 때문에 모든 부분 집합을 만들어 확인하려면 시간이 오래 걸리지만, 정수 i를 부분 집합에 포함시킬지 고려할 때 이미 부분 집합에 포함시킨 원소의 합 S와 아직 고려하지 않은 숫자들의 합 R을 동시에 활용하면 시간을 단축할 수 있다고 한다.

이를 활용해 M을 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, N과 K가 주어진다.

( 3<=N<=100, 6<=K<=모든 원소의 합 )

 


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.


"""

# 방법 3 -> dp로 풀기(부분 집합의 합을 구하는 방법)
T = int(input())

for t in range(T):
    N,K = map(int,input().split())
    nums = [i for i in range(1,N+1)]

    dp = [0] * (K+1)
    dp[0] = 1

    for num in nums:
        for i in range(K, num - 1, -1):  # 거꾸로 가는 이유는!!!! *** 중복을 방지하기 위해서임!!!!***
            dp[i] += dp[i - num]  # 이게 이제 합이 i가 되는 부분집합의 개수 아.. 그럼 dp[K]면 K가 될 때의 경우의 수만 세주겟구나

    print(f"#{t+1} {dp[K]}")  # 합이 K인걸 바로 찾아줌.

    """
    중복인 경우에는
    for num in nums:
        for i in range(1, targer+1):
            if i - num >= 0  # 이 조건 꼭 해주기 음수가 나올수도 잇으니까!
                dp[i] += dp[i - num]
    print(dp[K])
    
    """

# 방법 2 -> 백트래킹으로 찾기
# def back(start, total, path):
#     global count, K, N

#     if total == K:
#         count += 1
#         return 
#     if total > K:
#         return
    
#     for i in range(start, N+1):
#         back(i+1, total + i, path + [i])

# T = int(input())
# for t in range(T):
#     N, K = map(int,input().split())

#     count = 0

#     back(1,0,[])
#     print(count)

# 방법 1 -> combinations로 모든 부분집합 구해서 합이 K인 거 찾기
# from itertools import combinations
# T = int(input())
# for t in range(T):
#     N , K =map(int,input().split())

#     nums = [i for i in range(1,N+1)]

#     count = 0
#     for i in range(N):
#         for comb in combinations(nums,i):
#             if sum(comb) == K:
#                 count += 1
#     print(count)


                