import sys
sys.stdin = open("input.txt","r")

"""
알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.

5<=N<=1,000,000, 0 <= ai <= 1,000,000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.

예제1

2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

출력 1

#1 2 0
#2 6 6

"""
def merge_sort(arr):
    def sort(arr):
        nonlocal count
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = sort(arr[0:mid])
        right = sort(arr[mid:])

        if left[-1] > right[-1]:
            count += 1

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    count = 0
    sorted_arr = sort(arr)
    return sorted_arr, count


T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    sorted_arr, count = merge_sort(arr)

    print(f"#{t+1} {sorted_arr[N//2]} {count}")

