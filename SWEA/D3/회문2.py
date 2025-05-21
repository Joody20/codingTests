"""
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

출력 1
#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18

"""

import sys
sys.stdin = open("input.txt")

for t in range(1,11):
    N = int(input())
    lst = [list(input()) for _ in range(100)]
    
    max_len = 0

    for L in range(100,0,-1):
        found = False
        #가로
        for i in range(100):
            for j in range(0, 100 - L + 1):  # 회문의 길이 만큼
                sub = lst[i][j:j+L]  # 가로는 한줄로 되어 있으니까 바로 슬라이싱이 가능함.
                if sub == sub[::-1]:
                    found = True

        #세로
        for i in range(100):
            for j in range(0, 100 - L + 1):
                sub = []
                for q in range(L):  # 세로는 직접 인덱스를 넣어줘야됌.
                    sub.append(lst[j+q][i])
                if sub == sub[::-1]:
                    found = True

        if found:
            max_len = L
            break

    print(f"#{N} {max_len}")