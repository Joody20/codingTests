"""
백준 2075번(자료구조) 실버 2: N번째 큰 수 

heap을 써서 했어야 햇어....

메모리를 절약하고 싶을 때는 heap을 쓰도록 하자 다영

"""

import heapq
import sys
sys.stdin = open("input.txt" , "r")

N = int(input()) # N번째 큰수를 찾아서 리턴하면돼.

min_heap = []  # heap에 대한 빈 리스트 만들고

for _ in range(N):
    for num in map(int, input().split()):
        if len(min_heap) < N: # heap의 길이가 N보다 작으면
            heapq.heappush(min_heap, num) # min_heap에 num을 push해
        else: # N보다 길어지면
            heapq.heappushpop(min_heap,num) #min_heap에서 최소값을 지우고 num을 push해


print(min_heap[0]) # 저걸 다하고 나면 이제 최댓값 5개가 남을거 아니야 근데 N번째인걸 구해야 되니까 첫번째꺼이겟지 항상.

"""
여긴 이제 메모리 신경안쓰고 작성함.
numbers = [list(map(int, input().split())) for _ in range(N)]

nums = []

for n in numbers:
    for i in n:
        nums.append(i)

res = sorted(nums)[-N:-N+1]

print("".join(map(str, res)))

"""



