import sys
sys.stdin = open("input.txt",'r')

"""
문제
수직선과 같은 일직선상에 N개의 마을이 위치해 있다. i번째 마을은 X[i]에 위치해 있으며, A[i]명의 사람이 살고 있다.

이 마을들을 위해서 우체국을 하나 세우려고 하는데, 그 위치를 어느 곳으로 할지를 현재 고민 중이다. 고민 끝에 나라에서는 각 사람들까지의 거리의 합이 최소가 되는 위치에 우체국을 세우기로 결정하였다. 우체국을 세울 위치를 구하는 프로그램을 작성하시오.

각 마을까지의 거리의 합이 아니라, 각 사람까지의 거리의 합임에 유의한다.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 X[1], A[1], X[2], A[2], …, X[N], A[N]이 주어진다. 범위는 |X[i]| ≤ 1,000,000,000, 0 ≤ A[i] ≤ 1,000,000,000 이며 모든 입력은 정수이다.

모든 A[i]를 합친 값은 0보다 크다.

출력
첫째 줄에 우체국의 위치를 출력한다. 단, 답이 여러 개일 경우 우체국의 위치가 작은 것을 출력한다.


"""
N = int(input())
villages = [tuple(map(int, input().split()))for _ in range(N)]

#위치 기준 정렬
villages.sort()  

#전체 인구수
total_people = sum(pop for _,pop in villages)

#누적 인구수
acc = 0
for x ,pop in villages:
    acc += pop
    if acc >= total_people / 2:  # 전체 인구 수의 절반 이상이 되는 지점을 찾는거야.
        print(x)
        break