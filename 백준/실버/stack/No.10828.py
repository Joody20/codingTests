"""
백준 실버 4 = 스택 : https://www.acmicpc.net/problem/10828
"""
import sys
sys.stdin = open("input.txt", "r")

N = int(input())  # 줄의 개수

commands = [input().split() for _ in range(N)]  # 명령어들 불러오기

res = []

for i in range(len(commands)):
    if commands[i][0] == 'push':
        res.append(commands[i][1])

    elif commands[i][0] == 'pop':  # ***중요 나는 res.pop()한 후 이제 print(res.pop()) 이렇게 했는데 이러면 pop를 두번 부르는거기 때문에 저절로 두개가 한번에 처리된다. 그래서 if / else 문으로 나눠서 print할 때만 한번 Pop 실행할 수 있게끔.
        if len(res) == 0:
           print('-1')
        else:
            print(res.pop())

    elif commands[i][0] == "size":
        print(len(res))

    elif commands[i][0] == "empty":
        if len(res) == 0:
            print('1')
        else:
            print('0')

    elif commands[i][0] == 'top':
        if len(res) == 0:
            print('-1')
        else:
            print(res[-1])
