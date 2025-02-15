"""
백준 골드 5(문자열) : 문자열 게임 2
https://www.acmicpc.net/problem/20437

https://davincicoding.tistory.com/165 -> 도움이 됐던 블로그 !

예제1 
2
superaquatornado
2
abcdefghijklmnopqrstuvwxyz
5

예제2
1
abaaaba
3
"""


from collections import Counter
import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # T개의 케이스

for _ in range(T):
    string_data = input().rstrip()
    K = int(input())
    
    char_count = Counter(string_data) # 이건 이제 문자가 나타난 횟수

    cnt_dict = dict(char_count)   # char_count를 딕셔너리 형태로 바꿔줌.

    cnk_dict = {} # K개 이상을 포함한 문자들의 집합

    for i , c in enumerate(string_data):
        if cnt_dict[c] < K:
            continue
        cnk_dict[c] = cnk_dict.get(c, []) + [i]   # 이건 K개를 포함한 문자열들 

    Max = -1
    Min = len(string_data)

    for k , v in cnk_dict.items():
        # print(k,v)
        for i in range(len(v) - K + 1): # 아 K개를 포함하는 거여야 하니까...
            value_len = v[i + K - 1] - v[i] + 1 # v의 길이
            Max = max(Max, value_len) # 가장 긴 길이
            Min = min(Min, value_len) # 가장 짧은 길이


    if cnk_dict: # cnk_dict에 뭐가 있으면 
        print(Min, Max) # 그 때, 긴 것과 짧은 것을
    else: # cnk_dict이 비어 있으면 -1 리턴
        print('-1')

