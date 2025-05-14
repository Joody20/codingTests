import sys
sys.stdin = open("input.txt","r")

"""
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.

이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 A와 B에 속한 정수의 개수 N, M이 주어지고, 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수가 주어진다.

1<=N, M<=500,000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


예제 1
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5

출력 1
#1 2
#2 0
#3 3

"""
def binary(arr,target):
    left , right = 0,len(arr) - 1
    direction = 0 # 0: 시작, -1:왼쪽, 1:오른쪽

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        
        elif arr[mid] < target:
            if direction == 1:
                return False
            direction = 1
            left = mid + 1
        else:
            if direction == -1:
                return False
            direction = -1
            right = mid - 1

    return False

T = int(input())

for i in range(T):
    N, M = map(int,input().split())  # N은 arr_A의 길이, M은 arr_B의 길이

    arr_A = sorted(list(map(int,input().split())))
    arr_B = list(map(int,input().split()))

    count = 0
    for b in arr_B:
        if binary(arr_A , b):
            count += 1

    print(f"#{i+1} {count}")
        
            
        

    