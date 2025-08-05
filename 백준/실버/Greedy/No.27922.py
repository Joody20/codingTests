import sys
sys.stdin = open("input.txt","r")

"""

예제 1
3 2
2 4 10
55 8 2
1 9 5

출력 1
73

"""
from itertools import combinations

N,K = map(int,input().split())
lectures = [tuple(map(int,input().split())) for _ in range(N)]

max_result = 0

for i,j in [(0,1), (1,2),(0,2)]:  # 어쨌든 이게 지금 3개의 역량만 주어진거라 첫번째+두번째, 두번째+세번째, 첫번째+세번째한 값애서 이제 내림차순으로 정렬
    sorted_lectures = sorted(lectures, key=lambda x: x[i] + x[j], reverse=True)

    A = B = C = 0
    for a,b,c in sorted_lectures[:K]: # 상위 K개를 골라서
        A += a  # a역량은 a역량끼리 더하고
        B += b # b역량은 b역량끼리 더하고
        C += c  # c역량은 c역량끼리 더하고
 
    max_result = max(max_result, A + B, B + C, A + C)

print(max_result)




