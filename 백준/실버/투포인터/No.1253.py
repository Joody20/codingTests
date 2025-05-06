import sys
sys.stdin = open("input.txt","r")

"""
백준 좋다 : https://www.acmicpc.net/problem/1253

문제
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

입력
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

출력
좋은 수의 개수를 첫 번째 줄에 출력한다.

예제 1
10
1 2 3 4 5 6 7 8 9 10

출력 1
8

"""
N = int(input())
nums = list(map(int,input().split()))
nums.sort()

good = 0
for k in range(N):
    target = nums[k]   # 이 target점을 찾는게 어려웠고,
    start = 0 
    end = N-1   

    while start < end:

        # 자기자신은 피하기 위해
        if start == k:  
            start += 1
            continue
        if end == k:
            end -= 1
            continue

        cur_sum = nums[start] + nums[end]  # 현재의 합

        if cur_sum == target:  # 현재 합이 target과 같으면 good += 1
            good += 1
            break
        elif cur_sum < target:  # target값이 더 크면 start += 1
            start += 1
        else:  # 작으면 end -= 1
            end -= 1

print(good)






