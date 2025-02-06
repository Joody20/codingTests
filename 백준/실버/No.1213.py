"""
백준 실버 3 팰린드롬: https://www.acmicpc.net/problem/1213

예제:
ABCD
AABB
AAABB
ABACABA
"""

from collections import Counter
import sys
sys.stdin = open("input.txt", "r")


words = list(input().rstrip())

word_dict = Counter(words)  # 문자열의 개수를 파악해야됨.

word_part , center = [] , ''  # 각 자리, 가운데

if len(list(filter(lambda x: x % 2 != 0 , word_dict.values()))) > 1: # 일단 문자열의 개수가 홀수이고, 그 value가 1이상이면
    print("I'm Sorry Hansoo")  # 이 때는 팰린드롬 문자열을 만들 수 없음
    exit()

for k ,w in word_dict.items():
    if w % 2 != 0:  # w의 개수가 홀수이면
        word_part += ([k] * ((w-1) // 2))  # 그 문자 k를 여기에 두고
        center = k
    else:  # w의 개수가 짝수이면
        word_part += ([k] * (w // 2))  # k를 짝수 자리에 둠..

front = ''.join(sorted(word_part))  # 사전순으로 나열 해야돼서.
 
print(front+center+front[::-1])






## words[::-1] 하면 이제 문자열 거꾸로 하기...





