"""
백준 실버 2(자료구조) : 스택 수열
https://www.acmicpc.net/problem/1874

예제
8
4
3
6
8
7
5
2
1
"""


import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # N개의 수

nums = [int(input()) for _ in range(N)]

stack = []
res = [] # 부호 넣는 부분

current = 1 # stack에 푸시할 숫자  **나는 N길이의 정수를 담은 배열을 만들어서 그걸 넣는 느낌으로 하려고 했는데 생각해보니 그냥 숫자를 늘리면 됐음.
possi = True   # 수열이 가능한지 판단

for n in nums:
    while current <= n: # 현재 숫자가 n보다 작거나 같을 때 까지 반복
        stack.append(current) # stack에 현재 숫자를 넣고
        res.append('+') # 이제 res에 push한 만큼의 +를 넣고
        current += 1 # current는 하나씩 증가

    if stack[-1] == n: # 근데 만약 stack에 맨 마지막 숫자와 지금 현재 n과 같으면
        stack.pop() # 그 숫자 빼기
        res.append('-') # 그 만큼 - 넣기
    else: # 아예 수열을 만들 수 없는 경우
        possi = False # False로 해주고
        break # 끝

if possi: # 수열이 가능하다면
    print('\n'.join(res)) # 현재 res 배열에 있는 숫자를 들여쓰기로 print해줌
else: # 수열이 불가능하면
    print('NO') # No를 리턴해줌.
