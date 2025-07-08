"""
백준 실버 3(자료구조) : 빈도정렬
https://www.acmicpc.net/problem/2910

예제
5 2
2 1 2 1 2

9 3
1 3 3 3 2 2 2 1 1

9 77
11 33 11 77 54 11 25 25 33
"""

from collections import Counter
import sys
sys.stdin = open("input.txt", "r")


N , C = map(int, input().split())

nums = input().split()

count = Counter(nums)  # 빈도수 계산

res = []


data = list(count.items())  # 이걸 list 형태로 바꿨어야 했고

sorted_data = sorted(data, key=lambda x: -x[1])  # -x[1]로 하면 이제 내림차순 정렬 해주는거임 !!! ****** 반복문에 돌렸으면 안됐음 ㅠㅠㅠㅠ

# sorted_data = sorted( data , reverse= False)


for n , i in sorted_data:
    for _ in range(i):
        res.append(n)

print(' '.join(res))

