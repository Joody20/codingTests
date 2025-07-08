"""
백준 실버 4(자료구조) : 문자열 집합
"""

import sys
sys.stdin = open("input.txt", "r")


N , M = map(int, input().split())

S = [input().rstrip() for _ in range(N)] # 집합 문자열 S
words = [input().rstrip() for _ in range(M)] # 검사해야하는 문자들

count = 0

for w in words:
    if w in S:
        count += 1

print(count)

