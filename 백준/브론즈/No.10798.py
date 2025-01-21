"""
백준 브론즈 1 : https://www.acmicpc.net/problem/10798
"""

import sys
sys.stdin = open("input.txt", "r")


words = list(input().strip() for _ in range(5))


for j in range(15):  # 최대 한줄에 15개 단어까지 된다고 햇잔아
    for i in range(5):  # 총 5줄
        if j < len(words[i]):  # words[0], [1] 들의 길이가 지금 15보다 작으면
            print(words[i][j], end='')  # words[0][0] [1][1] 아 이렇게 .... 그리고 end='' 하면 공백없이 가로로 출력 가능 !!

