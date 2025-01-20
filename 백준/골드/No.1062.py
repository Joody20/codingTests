"""
백준 1062번 문제
https://www.acmicpc.net/problem/1062

"""

import sys
sys.stdin = open("input.txt", "r")

N , K = map(int,input().split())

if K < 5:  # 시작하는 단어가 "anta", 끝나는 단어가 "tica"  -> 즉, a , n , t, i ,c 는 배워야하고 즉 , K가 5보다 작으면 어떤 단어도 배울 수 없음.
    print(0)
    exit()
elif K == 26: # 26개이면 모든 단어를 배울 수 있음.
    print(N)
    exit()
    
answer = 0
words = [set(input().rstrip()) for _ in range(N)]  # 단어들을 가져온다. set은 중복 방지
learn = [0] * 26

for c in ('a' , 'n', 't', 'i', 'c'): # 이 5개의 단어는 무조건 배워야됌.
    learn[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
    global answer  # 전역변수로 두고

    if cnt == K - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer,readcnt)
        return
    
    for i in range(idx , 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0,0)
print(answer)


"""
// 백준 제출 코드

N, K = map(int, input().split())

if K < 5:  # Not enough characters to learn "antic"
    print(0)
    exit()
elif K == 26:  # All characters can be learned
    print(N)
    exit()

words = [input().rstrip() for _ in range(N)]
essential = set('antic')
word_masks = []

# Convert words to bitmasks
for word in words:
    mask = 0
    for char in set(word):  # Use only unique characters in the word
        mask |= (1 << (ord(char) - ord('a')))
    word_masks.append(mask)

# Initialize variables
answer = 0
essential_mask = sum(1 << (ord(c) - ord('a')) for c in essential)

# DFS function to learn characters
def dfs(idx, learned_mask, count):
    global answer
    if count == K - 5:  # Already learned K-5 extra characters
        readable = sum(1 for mask in word_masks if (mask & ~learned_mask) == 0)
        answer = max(answer, readable)
        return

    for i in range(idx, 26):
        if not (learned_mask & (1 << i)):  # If character `i` is not yet learned
            dfs(i + 1, learned_mask | (1 << i), count + 1)

# Start DFS from index 0 with the essential characters already learned
dfs(0, essential_mask, 0)
print(answer)

"""