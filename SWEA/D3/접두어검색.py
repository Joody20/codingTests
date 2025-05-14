import sys
sys.stdin = open("input.txt","r")

"""
문자열 about에서 첫 글자부터 이어지는 a, ab, abo, abou, about은 접두어이다.

단, abu 같이 첫 글자부터 계속 이어지는 경우가 아니면 접두어가 아니다.

문자열 그룹 A와 B가 주어질 때, B에 속한 문자열 중 A의 접두어인 문자열의 개수를 알아내는 프로그램을 만드시오. 모든 단어는 소문자로 이루어져 있다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 A의 단어 개수 N과 B의 단어개수 M이 주어진다.

다음 줄부터 N개의 단어와 M개의 단어가 주어진다.

( 1<=T<=50, 3<=N, M<=3000 ) 

단어의 길이는 20글자 이내이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.


예제 1

2
3 3
able
abl
abroad
ab
abo
a
3 5
people
water
night
wa
h
country
ni
people

출력 1

#1 2
#2 3

"""
T = int(input())

for t in range(T):
    N , M = map(int,input().split())
    arrA = []
    for _ in range(N):
        arrA.append(input())

    arrB = []
    for _ in range(M):
        arrB.append(input())


    subsets = set()
    for a in arrA:
        for j in range(1, len(a)+1):
            subsets.add(a[:j])

    print(subsets)

    count = 0
    for b in arrB:
        if b in subsets:
            count += 1

    print(f"#{t+1} {count}")



