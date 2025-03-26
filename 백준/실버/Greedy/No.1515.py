"""
백준 수이어쓰기(실버 3): https://www.acmicpc.net/problem/1515


"""
import sys
sys.stdin = open("input.txt","r")

nums = input()
n = 0
idx = 0
while True:
    n += 1
    for s in str(n):
        if nums[idx] == s:
            idx += 1
            if idx >= len(nums):
                print(n)
                exit()


