import sys
sys.stdin = open("input.txt","r")

"""
A와 B는 각자 만든 영어 단어장에 같은 단어가 얼마나 있는지 확인하려고 한다.

두 사람이 만든 단어장에 공통으로 들어있는 단어의 개수를 알아내는 프로그램을 만드시오. 단, 모든 단어는 소문자로 되어 있다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 A의 단어 개수 N과 B의 단어개수 M이 주어진다. 다음 줄부터 N개의 단어와 M개의 단어가 주어진다.

(1<=T<=50, 3<=N, M<=3000)

단어의 길이는 20글자 이내이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.


"""
T = int(input())

for t in range(T):
    N, M =map(int,input().split())

    arrA = [input() for _ in range(N)]
    arrB = [input() for _ in range(M)]

    count = 0
    for a in arrA:
        if a in arrB:
            count += 1

    print(f"#{t+1} {count}")
