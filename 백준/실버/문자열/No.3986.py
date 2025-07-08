"""
백준 실버 3 : 좋은 단어 https://www.acmicpc.net/problem/3986


예제
3
ABAB
AABB
ABBA

"""

import sys
sys.stdin = open("input.txt", "r")

N = int(input())

count = 0

words = [input().rstrip() for _ in range(N)]

for word in words:
    res = []
    for w in word:
        if res and w == res[-1]:
            res.pop()
        else:
            res.append(w)

    if not res:
        count += 1

print(count)