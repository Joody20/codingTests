import sys
sys.stdin = open("input.txt","r")

"""
N개의 서로 다른 자연수를 원소로 갖는 집합에서, 부분집합을 만들었다.

이때 원소 사이의 순서가 원래 집합에서의 순서와 일치하고, 오름 차순 정렬을 해도 원소의 순서가 바뀌지 않는 경우가 있다.

이 중 원소의 개수가 가장 많은 부분집합의 원소 개수를 출력하는 프로그램을 만드시오.

예를 들어 처음 주어진 집합이 {1, 3, 2, 4}인 경우 조건에 해당하는 부분 집합은 {1, 3, 4}와 {1, 2, 4}이므로, 원소의 개수는 3이 된다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, 원소의 개수 N과 N개의 자연수 ai가 한 줄에 주어진다.

1<=T<=50, 1<=N, i<=1000, 1<=ai<=N

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

예제 1
3
5 1 5 3 4 2
5 4 3 5 1 2
10 2 9 5 1 10 6 3 4 8 7

출력 1
#1 3
#2 2
#3 4

"""
# 방법 3 -> dp로 LIS 알고리즘 구현
T = int(input())
for t in range(T):
    lst = list(map(int,input().split()))
    N = lst[0]
    nums = lst[1:]

    dp = [1] * N  # LIS 배열을 저장하는 배열

    for i in range(N):
        for j in range(i):  #다영아 여기 i까지 해줘야지...ㅠㅠㅠㅠㅠㅠㅠㅠ
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+ 1)

    print(f"#{t+1} {max(dp)}")




#방법 1 -> LIS 알고리즘 사용 -> 가장 긴 증가하는 부분수열을 구하는거임.
# import bisect

# T = int(input())
# for t in range(T):
#     lst = list(map(int,input().split()))
#     N = lst[0]
#     nums = lst[1:]

#     dp = []  # LIS 배열을 저장하는 배열

#     for num in nums:
#         idx = bisect.bisect_left(dp,num)
#         if idx == len(dp):
#             dp.append(num)
#         else:
#             dp[idx] = num

#     print(f"#{t+1} {len(dp)}")




# 방법 2
# T = int(input())
# for t in range(T):
#     lst = list(map(int,input().split()))
#     N = lst[0]
#     nums = lst[1:]

#     lengths = []

#     for i in range(1 << N):
#         subset = []
#         for j in range(N):
#             if i & (1 << j):
#                 subset.append(nums[j])

#         # print(subset)  # 이 subset에서 오름차순인 subset만 골라내면되거든..?
#         if subset == sorted(subset):
#             lengths.append(len(subset))

#     print(f"#{t+1} {sorted(lengths,reverse=True)[0]}")

