"""
 백준 실버 4(자료구조) : 큐

 예제
 15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

"""

import sys
sys.stdin = open("input.txt", "r")


N = int(input())

Q = [input().split() for _ in range(N)]  # 이걸 split으로 했어야 됐다는것.


res = [] # 이게 큐가 되는거임

for q in range(len(Q)):

    if Q[q][0] == 'push':  # 앞에 있는 명령어를 빼내기 위해 이런식으로 함.
        res.append(Q[q][1])

    elif Q[q][0] == 'pop':
        if not res:
            print('-1')
        else:
            print(res.pop(0))

    elif Q[q][0] == 'size':
        print(len(res))
    
    elif Q[q][0] == 'empty':
        if not res:
            print('1')
        else:
            print('0')

    elif Q[q][0] == 'front':
        if not res:
            print('-1')
        else:
            print(res[0])

    elif Q[q][0] == 'back':
        if not res:
            print('-1')
        else:
            print(res[-1])
