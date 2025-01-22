"""
백준 브론즈 1 : https://www.acmicpc.net/problem/1157
"""

from collections import Counter
import sys
sys.stdin = open("input.txt", "r")


alphabets = list(input().strip().upper()) # 애초에 아예 대문자로...하면 ㅠㅠㅠ 되자나ㅠㅠㅠㅠㅠㅠ 멍청아ㅠㅠㅠㅠㅠ


# 단어의 빈도 개수
count = Counter(alphabets)
most_common = count.most_common(2)


if len(most_common) < 2:  # 이 땐, 무조건 이제 제일 빈도수가 많은거고
    print(most_common[0][0])
elif most_common[0][1] == most_common[1][1]:  # 최대빈도수가 여러개인 경우
    print('?')
else:  # 아무것도 아닌 이제 걍 어쨌든 리턴
    print(most_common[0][0])