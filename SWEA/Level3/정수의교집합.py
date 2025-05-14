import sys
sys.stdin = open("input.txt","r")
"""
프로그래머 알고씨는 그룹 A와 그룹 B에 모두 들어있는 정수의 개수를 알아내려고 한다.

A의 모든 정수를 B의 모든 정수와 비교해서 답을 얻을 수 있지만 확인해야 하는 최대 개수가 50만개라 다른 방법을 찾아야 한다.

알고씨는 인터넷 검색을 통해 파이썬의 Set을 사용하면 쉽게 답을 찾을 수 있다는 힌트를 얻었다.

이 힌트를 활용해 두 그룹에 모두 들어있는 정수의 개수를 알아내는 프로그램을 만드시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 A와 B에 속한 정수의 개수 N, M이 주어지고, 두 줄에 걸쳐 N개의 정수와 M개의 정수가 주어진다.

1<=N, M<=500,000
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

"""
T = int(input())


for i in range(T):
    N, M = map(int,input().split())
    arr_a = sorted(set(map(int,input().split())))
    arr_b = sorted(set(map(int,input().split())))

    count = 0
    for b in arr_b:
        if b in arr_a:
            count += 1
        else:
            continue
    print(f"#{i+1} {count}")