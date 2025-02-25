"""
백준 골드 4 (문자열 ) : 비슷한 단어


예제 1
9
noon
is
lunch
for
most
noone
waits
until
two

예제 2
4
abcd
abe
abc
abchldp

"""

import sys
sys.stdin = open("input.txt" , "r")

N = int(input())

def similarity(s1, s2):
    set_1 , set_2 = set(s1) , set(s2)
    common_s = len(set_1 & set_2)
    return common_s / max(len(set_1), len(set_2))  # 유사도 계산이래

words = [input().rstrip() for _ in range(N)]
max_sim = -1
pair = None

for i in range(len(words)):
    for j in range(i + 1 , len(words)):
        sim = similarity(words[i], words[j])
        if sim > max_sim:
            max_sim = sim
            pair = [words[i] , words[j]]
    
print("\n".join(pair))
