import sys
sys.stdin = open("input.txt","r")

"""
문제
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.

예제 1
9
5 12 7 10 9 1 2 3 11
13

출력 1
3

"""
N = int(input())
nums = list(map(int,input().split()))
x = int(input())

i = 0
j = N-1
count = 0

nums.sort()

while i < j:
    if (nums[i]+nums[j]) < x:  # 더한게 x보다 작으면, i를 하나씩 늘려주고,
        i += 1
    elif (nums[i]+nums[j]) > x: # 더한게 x보다 크면, j를 하나씩 줄여주고
        j -= 1
    elif (nums[i]+nums[j]) == x: # x랑 같으면, count 증가, i 증가, j증가
        count += 1
        i += 1
        j -= 1

print(count)






