"""
백준 부분수열의 합(실버2) : https://www.acmicpc.net/problem/1182

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 1
5 0
-7 -3 -2 5 8

출력 1
1

"""
import sys
sys.stdin = open("input.txt","r")

N , S = map(int,input().split())
nums = list(map(int,input().split())) 
result = []
count = 0


def back(s):
    global count
    if sum(result) == S and len(result) > 0:
        count += 1
    for i in range(s,N):
        result.append(nums[i])
        back(i+1)
        result.pop()

back(0)
print(count)


