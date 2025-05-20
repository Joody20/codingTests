import sys
sys.stdin = open("input.txt","r")

"""
N개의 10억 이하 자연수로 이뤄진 수열이 주어진다. 이 수열은 완성된 것이 아니라 M번의 편집을 거쳐 완성된다고 한다.

완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.

다음은 미완성 수열과 편집의 예이다.

만약 편집이 끝난 후 L이 존재하지 않으면 -1을 출력한다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.

그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다. 5<=N<=1000, 1<=M<=1000, 6<=L<=N+M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

예제 1
3
5 3 4
1 2 3 4 5
I 2 7
D 4
C 3 8
5 5 2
15171 7509 20764 13445 10239
C 3 18707
C 1 20250
D 2
D 2
C 0 7158
10 10 8
27454 29662 2491 1819 10118 15441 7357 23618 972 398
D 7
D 1
D 6
I 3 2906
C 1 27121
D 3
D 2
D 1
D 2
C 2 20794

출력 1

#1 5
#2 10239
#3 -1

"""
T=int(input())
for t in range(T):
    N, M, L = map(int,input().split())
    arr = list(map(int,input().split()))
    edits = []
    for _ in range(M):
        edits.append(input().split())

    for edit in edits:
        op = edit[0]   # 연산 'I'면 추가, 
        nums= list(map(int,edit[1:]))

        if op == 'I' and len(nums) > 1:
            idx = nums[0]
            num = nums[1]
            arr.insert(idx,num)
        elif op == 'D' and len(nums) == 1:
            num = nums[0]
            arr.pop(num)
        elif op =='C' and len(nums) > 1:
            idx = nums[0]
            num = nums[1]
            arr[idx] = num

    if len(arr) >= L:
        print(f"#{t+1} {arr[L]}")
    else:
        print(f"#{t+1} {-1}")