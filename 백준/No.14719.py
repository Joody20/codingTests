import sys
sys.stdin = open("input.txt", "r")

"""
    백준 14719번(골드5) = https://www.acmicpc.net/problem/14719
"""


H , W  = map(int,input().split()) # 높이와 가로
height_list = list(map(int,input().split())) # 블록의 개수

maxHeight = height_list[0]

maxPosition = 0
accumHeight = 0

rains = 0

for i in range(1 , W -1):
    curHeight = height_list[i]  # 현재 블록의 높이
    beforeHeight = height_list[i-1] # 전꺼의 블록의 높이
    nextHeight = height_list[i+1] # 다음꺼의 블록의 높이

    # print(beforeHeight , curHeight , nextHeight)

    leftMaxHeight = max(height_list[:i])  # 현재 height에서 왼쪽 height 값이 가장 큰 거
    rightMaxHeight = max(height_list[i:]) # 현재 height 값에서 오른쪽 height 값이 가장 큰 거

    if curHeight < leftMaxHeight and curHeight < rightMaxHeight: # 현재의 높이가 왼쪽,오른쪽높이보다 작으면
        minHeight = min(leftMaxHeight , rightMaxHeight)  # 왼쪽, 오른쪽 높이의 가장 큰 값에서 min 값을 구해서

        rains += (minHeight - curHeight) # 현재 높이와 가장 작은 높이의 값을 빼서 다 더함.

print(rains) # 최종적인 빗물의 고인 양


