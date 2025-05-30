"""
백준 골드 4 공유기 설치 : https://www.acmicpc.net/problem/2110

도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.


첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.


예제 1
5 3
1
2
8
4
9

출력 1
3

"""
import sys
sys.stdin = open("input.txt","r")

N , C = map(int,input().split())

arr = []
for _ in range(N):
    x = int(input())
    arr.append(x)

arr.sort()  # 배열을 오름차순 정렬해주고,

start = 1 # 공유기 거리 최소
end = arr[-1] - arr[0] # 공유기 거리 최대
result = 0 # 결과값

while start <= end:
    mid = (start + end) // 2
    current = arr[0]
    count = 1  # 공유기 설치 대수 

    # 공유기 설치 몇대까지 할 수 있는지 체크
    for i in range(1,N):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]

    # 공유기 설치대수가 목표 개수보다 크면 
    if count >= C:
        start = mid + 1  # start를 더 뒤로 미룸 -> 공유기 사이 거리를 더 늘리는거임.
        result = mid
    else:  # 작으면
        end = mid - 1  # end를 앞으로 땡김 -> 공유기 사이 거리를 줄이는거임.

print(result)

