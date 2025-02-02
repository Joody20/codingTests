"""
백준 실버 3 : 영단어 암기는 괴로워 https://www.acmicpc.net/problem/20920
"""

from collections import Counter
import sys
sys.stdin = open("input.txt", "r")


N , M = map(int,input().rstrip().split())  #N은 단어의 개수 , M 은 외울 단어의 길이의 기준 !!

# words  = set(input().strip() for _ in range(N))  # 이렇게 하면 중복되는 단어 없이 나온 단어만 가져올 수 있음.


words = []

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words.append(word)

# res = [] # 단어장에 넣을 단어

count = Counter(words)

words = list(count)

sorted_words = sorted(count.items() , key= lambda x : (-x[1], -len(x[0]), x[0]))

res = [word for word , count in sorted_words if len(word) >= M]

# print(sorted_words)
print("\n".join(res))

# for i in sorted_words:
#     print(i)






"""
//백준 통과 코드
import sys
from collections import Counter
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
l = []
for i in range(n):
    t = input().rstrip()
    if len(t)>=m :l.append(t)
c = Counter(l)
l = list(c)
c2 = sorted(c.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in range(len(c2)):print(c2[i][0])
"""

