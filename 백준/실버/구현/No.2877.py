import sys
sys.stdin = open("input.txt","r")
"""
문제
창영이는 4와 7로 이루어진 수를 좋아한다. 창영이가 좋아하는 수 중에 K번째 작은 수를 구해 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 K(1 ≤ K ≤ 109)가 주어진다.

출력
첫째 줄에 창영이가 좋아하는 숫자 중 K번째 작은 수를 출력한다.

예제 1
1
출력 1
4

예제 2
2
출력 2
7

예제 3
3
출력 3
44

"""
from collections import deque
n = int(input())

queue = deque(["4","7"])
count = 0
while queue:
    cur = queue.popleft()
    count += 1
    if count == n:
        print(int(cur))
        break
    queue.append(cur+"4")
    queue.append(cur + "7")

"""
result = ''
while N > 0:
    m = N % 2  # 짝수 
    N = N // 2
    if m == 0:
        N-=1
        result = '7' + result
    else:
        result = '4' + result

print(result)

"""


