import sys
sys.stdin = open("input.txt","r")


"""
문제
영선이는 이번에 편의점으로 창업을 하려고 계획 중이다. 이번 창업을 위해 많은 준비를 하고 있는데, 아직 편의점을 세울 위치를 결정을 하지 못했다. 영선이는 미리 시장조사를 하여, 주요 고객들이 어느 위치에 존재하는지 파악을 하였고, 모든 고객들의 거리의 합을 최소로 하려한다. 두 위치 (x1, y1), (x2, y2)의 거리는 |x1 - x2| + |y1 - y2|로 정의한다.

n명의 주요 고객들의 위치 (xi, yi)이 주어질 때, 모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때, 그 최소 거리 합을 출력하시오.

입력
첫째 줄에는 주요 고객들의 수 n이 주어진다.

다음 n줄에는 i번 고객의 위치 xi, yi가 주어진다.

출력
모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때, 그 최소 거리 합을 출력하시오.

예제
5
2 2
3 4
5 6
1 9
-2 -8

출력 
30

"""

N = int(input())

x_lst = []
y_lst = []

for _ in range(N):
    x, y = map(int,input().split())

    x_lst.append(x)
    y_lst.append(y)

#x,y좌표 분리해서 정렬시키기
x_sorted = sorted(x_lst)
y_sorted = sorted(y_lst)


# 중앙값 찾기
x_median = x_sorted[N // 2]
y_median = y_sorted[N // 2]

# 거리계산하기
total = 0
for xx,yy in zip(x_lst,y_lst):
    # 거리계산 |x-2| + |y-4| -> 이런식으로 계산해주는거임. 각 위치마다 중간값과 x,y값계산
    distance = abs(xx - x_median) + abs(yy - y_median)
    total += distance  # 각 위치의 총 거리의 값

print(total)


    



